from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import DetailView

from market.models.book import Book

from market.models.author import Author

from market.models.category import Category


def all_books(request):
    books_list = Book.objects.all()
    authors = Author.objects.all()
    categories = Category.objects.all()

    # Get filter parameters from GET request
    category_id = request.GET.get('category')
    author_id = request.GET.get('author')
    price_order = request.GET.get('price_order')

    print("Author name:", author_id)  # Debugging statement

    # Apply filtering based on parameters
    if category_id:
        books_list = books_list.filter(category__id=category_id)
        authors = authors.filter(book__category__id=category_id).distinct()
        categories = categories.filter(book__id__in=books_list.values_list('id')).distinct()

    if author_id:
        books_list = books_list.filter(author__id=author_id)
        categories = categories.filter(book__author__id=author_id).distinct()
        authors = authors.filter(book__id__in=books_list.values_list('id')).distinct()
        print("Filtered books count:", books_list.count())  # Debugging statement

    if price_order == 'asc':
        books_list = books_list.order_by('price')
    elif price_order == 'desc':
        books_list = books_list.order_by('-price')

    # Paginate the filtered books
    paginator = Paginator(books_list, 3)  # Show 3 books per page.
    page_number = request.GET.get('page')  # Get the current page number from the request
    books = paginator.get_page(page_number)  # Get the books for the requested page

    # Pass the paginated queryset to the template context
    return render(request, 'book/book.html', {'books': books, 'categories': categories, 'authors': authors})


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
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