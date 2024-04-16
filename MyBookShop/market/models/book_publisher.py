from django.db import models
from django.utils.translation import gettext_lazy as _

from market.models.book import Book
from market.models.publisher import Publisher


class BookPublisher(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_("book"))
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name=_("publisher"))
    publication_date = models.DateField(verbose_name=_("publication date"))
    edition = models.CharField(max_length=100, verbose_name=_("edition"), blank=True, null=True)
    published_copies = models.IntegerField(verbose_name=_("published copies"), blank=True, null=True)

    class Meta:
        verbose_name = _("book publisher")
        verbose_name_plural = _("book publishers")

    def __str__(self):
        return f"{self.book.title} - {self.publisher.name}"