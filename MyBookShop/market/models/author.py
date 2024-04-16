
from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("author name"))
    birth_date = models.DateField(verbose_name=_("birth date"))
    birth_place = models.CharField(max_length=100, verbose_name=_("birth place"))
    death_date = models.DateField(verbose_name=_("death date"), null=True, blank=True)
    death_place = models.CharField(max_length=100, verbose_name=_("death place"), null=True, blank=True)
    portrait = models.ImageField(upload_to='portraits/', blank=True, verbose_name=_("author portrait"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))

    class Meta:
        ordering = ['name']
        verbose_name = _("author")
        verbose_name_plural = _("authors")

    def __str__(self):
        return self.name

