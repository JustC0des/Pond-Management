from django.contrib import admin
from django.urls import path, reverse_lazy
from leaflet.admin import LeafletGeoAdmin
from pond_management.models import Pond, FishSpecies, Fish, PondFish
from pond_management.views import MyClassBasedView
import unfold.admin
from pond_management.forms import PondFishForm
from django.db.models import Sum, Subquery, OuterRef
from django.db.models import F

def duplicate_ponds(modeladmin, request, queryset):
    for pond in queryset:
        pond.pk = None
        pond.name = f"{pond.name} (Copy)"
        pond.save()

duplicate_ponds.short_description = "Duplicate selected ponds"

class CustomAdmin(LeafletGeoAdmin, unfold.admin.ModelAdmin):
    fields = ('name', 'location')
    list_display = ('name',)
    search_fields = ('name', 'location')

@admin.register(Pond)
class PondAdmin(CustomAdmin):
    actions = [duplicate_ponds]

@admin.register(FishSpecies)
class FishSpeciesAdmin(unfold.admin.ModelAdmin):
    fields = ('species',)
    list_display = ('species',)
    search_fields = ('species',)

@admin.register(Fish)
class FishAdmin(unfold.admin.ModelAdmin):
    fields = ('species', 'kind', 'length', 'price')
    list_display = ('species', 'kind', 'length', 'price')
    search_fields = ('kind', 'species__species', 'length', 'price')


from django.db.models import Sum, Subquery, OuterRef, Window
from django.db.models.functions import Coalesce, FirstValue
from django.db.models.expressions import F

@admin.register(PondFish)
class PondFishAdmin(unfold.admin.ModelAdmin):
    """Admin class for PondFish model."""
    form = PondFishForm
    fields = ('pond', 'Fish', 'quantity')
    list_display = ('pond', 'Fish', 'total_quantity')
    search_fields = ('pond__name', 'Fish__name')
    list_filter = ('pond', 'Fish')
    sortable_by = ('pond', 'Fish', 'quantity')

    class Media:
        css = {
            'all': ('admin/css/quantity_selector.css',)
        }
        js = ('admin/js/quantity_selector.js',)

    def get_queryset(self, request):
        """Override queryset to show unique pond-fish combinations with summed quantities."""
        # Create subquery for total quantities
        quantity_sum = PondFish.objects.filter(
            pond=OuterRef('pond'),
            Fish=OuterRef('Fish')
        ).values('pond', 'Fish').annotate(
            total=Sum('quantity')
        ).values('total')[:1]

        # Get base queryset and annotate with totals
        queryset = super().get_queryset(request)
        return queryset.select_related('pond', 'Fish')\
                      .annotate(total_quantity=Coalesce(
                          Subquery(quantity_sum),
                          0
                      ))\
                      .order_by('pond', 'Fish')\
                      .distinct('pond', 'Fish')

    def total_quantity(self, obj):
        """Display the total quantity for each pond-fish combination."""
        return obj.total_quantity
    total_quantity.short_description = 'Quantity'

    def get_urls(self):
        """Return custom URLs for the admin."""
        return super().get_urls() + [
            path(
                "custom-url-path",
                self.admin_site.admin_view(MyClassBasedView.as_view(model_admin=self)),
                name="custom_view",
            ),
        ]