from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("book title"))
    author = models.CharField(max_length=100, verbose_name=_("author name"))
    category = models.CharField(max_length=100, verbose_name=_("book category"))
    year = models.IntegerField(verbose_name=_("publication year"))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("book price"))
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name=_("book cover"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))

    def __str__(self):
        return self.title
