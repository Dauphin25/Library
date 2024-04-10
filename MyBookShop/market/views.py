from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView


# Create your views here.
def all_books(request):
    books_list = Book.objects.all()
    paginator = Paginator(books_list, 3)  # Show 3 books per page.

    page_number = request.GET.get('page')
    books = paginator.get_page(page_number)
    return render(request, 'book.html', {'books': books})


def home_page(request):
    return render(request, 'main.html')


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
