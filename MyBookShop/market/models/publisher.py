from django.db import models
from django.utils.translation import gettext_lazy as _


class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("publisher name"))
    founded_year = models.IntegerField(verbose_name=_("founded year"))
    country = models.CharField(max_length=100, verbose_name=_("country"))
    website = models.URLField(max_length=200, verbose_name=_("website"), blank=True, null=True)
    email = models.EmailField(max_length=100, verbose_name=_("email"), blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = _("publisher")
        verbose_name_plural = _("publishers")

    def __str__(self):
        return self.name