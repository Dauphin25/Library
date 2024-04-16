from django.shortcuts import render
from market.models.book import Book

from market.models.author import Author


def home_page(request):
    # Get the three most recent books
    famous_books = Book.objects.order_by('?')[:3]

    # Get the three most recent authors
    famous_authors = Author.objects.order_by('?')[:3]

    return render(request, 'home/home.html', {'books': famous_books, 'authors': famous_authors})