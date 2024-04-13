from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book, Author
from django.views.generic import DetailView


# Create your views here.
def all_books(request):
    books_list = Book.objects.all()
    paginator = Paginator(books_list, 3)  # Show 3 books per page.

    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'book.html', {'books': books})


def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})


def home_page(request):
    # Get the three most recent books
    famous_books = Book.objects.order_by('?')[:3]

    # Get the three most recent authors
    famous_authors = Author.objects.order_by('?')[:3]

    return render(request, 'home.html', {'books': famous_books, 'authors': famous_authors})


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


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'
    pk_url_kwarg = 'author_id'
    query_pk_and_slug = True
    slug_field = 'name'
    slug_url_kwarg = 'author_name'
    extra_context = {}
    extra_context['title'] = 'Author Detail'
    extra_context['header'] = 'Author Detail'
    extra_context['description'] = 'This is the detail of the author'
    extra_context['keywords'] = 'author, detail, author detail'