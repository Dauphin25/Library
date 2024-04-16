
from django.db import models
from django.utils.translation import gettext_lazy as _


from market.models.author import Author
from market.models.category import Category
from market.choices.covers import COVER_CHOICES


class Book(models.Model):

    title = models.CharField(max_length=100, verbose_name=_("book title"))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_("author"), null=True, blank=True)
    category = models.ManyToManyField(Category, verbose_name=_("book categories"), blank=True)
    year = models.IntegerField(verbose_name=_("publication year"))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("book price"))
    cover = models.ImageField(upload_to='covers/', blank=True, verbose_name=_("book cover"))
    cover_type = models.CharField(max_length=10, choices=COVER_CHOICES, default='other')  # Cover type of the book
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))

    class Meta:
        ordering = ['title']
        verbose_name = _("book")
        verbose_name_plural = _("books")

    def __str__(self):
        return self.title
