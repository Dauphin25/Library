from django.urls import path
from market.views import author as authors
from market.views import book as books
from market.views import home as home

urlpatterns = [
    path('', home.home_page, name='home'),
    path('book/', books.all_books, name='all_books'),
    path('author/', authors.all_authors, name='all_authors'),
    path('books/<int:book_id>/', books.BookDetailView.as_view(), name='book_detail'),
    path('authors/<int:author_id>/', authors.AuthorDetailView.as_view(), name='author_detail'),
]
