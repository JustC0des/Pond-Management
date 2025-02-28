from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db.models import PolygonField
from django.db import models

class Pond(models.Model):
    """Model representing a pond."""
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    location = PolygonField(verbose_name=_("Location"))

    def __str__(self) -> str:
        """String representation of the Pond model."""
        return self.name

    class Meta:
        """Meta options for the Pond model."""
        verbose_name = _("Pond")
        verbose_name_plural = _("Ponds")


class FishSpecies(models.Model):
    """Model representing a fish species."""
    id = models.BigAutoField(primary_key=True)
    species = models.CharField(
        max_length=100,
        verbose_name=_("Species")
    )

    def __str__(self) -> str:
        """String representation of the FishSpecies model."""
        return self.species

    class Meta:
        """Meta options for the FishSpecies model."""
        verbose_name = _("Fish species")
        verbose_name_plural = _("Fish species")


class Fish(models.Model):
    """Model representing a fish."""
    id = models.BigAutoField(primary_key=True)
    kind = models.CharField(
        max_length=100,
        null=False,
        verbose_name=_("Kind"),
        help_text=_("The kind of a fish (such as K1, K2)")
    )
    species = models.ForeignKey(FishSpecies, on_delete=models.CASCADE, verbose_name=_("Species"))
    length = models.CharField(max_length=100, verbose_name=_("Length Range"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))

    def __str__(self) -> str:
        """String representation of the Fish model."""
        return self.kind

    class Meta:
        """Meta options for the Fish model."""
        verbose_name = _("Fish")
        verbose_name_plural = _("Fishes")
        constraints = [
            models.UniqueConstraint(
                fields=['kind', 'species'],
                name='unique_kind_species'
            )
        ]


class PondFish(models.Model):
    """Model representing the relationship between a pond and a fish."""
    id = models.BigAutoField(primary_key=True)
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE, verbose_name=_("Pond"))
    Fish = models.ForeignKey(Fish, on_delete=models.CASCADE, verbose_name=_("Fish"))
    quantity = models.IntegerField(verbose_name=_("Quantity"))

    def __str__(self) -> str:
        """String representation of the PondFish model."""
        return f"{self.pond} - {self.Fish}"

    class Meta:
        """Meta options for the PondFish model."""
        verbose_name = _("Pond Fish")
        verbose_name_plural = _("Pond Fishes")