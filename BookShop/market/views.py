from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView


# Create your views here.
def all_books(request):
    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'
    query_pk_and_slug = True
    slug_field = 'title'
    slug_url_kwarg = 'book_title'
    extra_context = {}
    extra_context['title'] = 'Book Detail'
    extra_context['header'] = 'Book Detail'
    extra_context['description'] = 'This is the detail of the book'
    extra_context['keywords'] = 'book, detail, book detail'
    extra_context['author'] = 'BookShop'
