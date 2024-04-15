from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Book, Author, Category
from django.views.generic import DetailView


# Create your views here.
def all_books(request):
    # Get all books from the database
    books_list = Book.objects.all()
    categories = Category.objects.all()

    # Get filter parameters from GET request
    cover_type = request.GET.get('cover_type')
    category_id = request.GET.get('category')
    author_name = request.GET.get('author_name')
    max_price = request.GET.get('max_price')

    # Apply filtering based on parameters
    if category_id:
        books_list = books_list.filter(category__id=category_id)
    if cover_type:
        books_list = books_list.filter(cover_type=cover_type)
    if author_name:
        books_list = books_list.filter(author__name__icontains=author_name)
    if max_price:
        books_list = books_list.filter(price__lte=max_price)

    # Order books by price in descending order
    books_list = books_list.order_by('-price')

    # Paginate the filtered books
    paginator = Paginator(books_list, 3)  # Show 3 books per page.
    page_number = request.GET.get('page')  # Get the current page number from the request
    books = paginator.get_page(page_number)  # Get the books for the requested page

    # Pass the paginated queryset to the template context
    return render(request, 'book.html', {'books': books, 'categories': categories})


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