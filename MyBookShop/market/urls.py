from django.urls import path
from market import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('book/', views.all_books, name='all_books'),
    path('author/', views.all_authors, name='all_authors'),
    path('books/<int:book_id>/', views.BookDetailView.as_view(), name='book_detail'),
    path('authors/<int:author_id>/', views.AuthorDetailView.as_view(), name='author_detail'),
]
