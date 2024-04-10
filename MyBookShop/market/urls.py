from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('book/', views.all_books, name='all_books'),
    path('books/<int:book_id>/', views.BookDetailView.as_view(), name='book_detail'),
]
