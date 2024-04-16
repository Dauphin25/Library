
from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("category name"))
    description = models.TextField(verbose_name=_("description"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))

    class Meta:
        ordering = ['name']
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name



