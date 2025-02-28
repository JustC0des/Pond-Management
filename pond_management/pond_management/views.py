from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from unfold.views import UnfoldModelAdminViewMixin
from django.core.serializers import serialize
from django.db.models import Sum
from .models import Pond, PondFish

@method_decorator(staff_member_required, name='dispatch')
class MyClassBasedView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Map"
    permission_required = (
        "pond_management.view_pond",
        "pond_management.add_pond",
        "pond_management.change_pond",
        "pond_management.delete_pond",
    )
    template_name = "admin/custom_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ponds_geojson'] = serialize('geojson', Pond.objects.all())
        context['PondFish_data'] = list(
            PondFish.objects.values(
                'pond__name', 
                'Fish__kind',
                'Fish__species__species'
            ).annotate(
                total_quantity=Sum('quantity')
            ).order_by('pond__name', 'Fish__kind')
        )
        return context