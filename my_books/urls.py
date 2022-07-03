from django.urls import path
from .views import *

urlpatterns = [
    path('', UserBooksList.as_view(), name='my_books'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book'),
    path('add_new_book/', AddNewBook.as_view(), name='add_new_book'),
    path('book_update/<int:pk>/', UpdateBook.as_view(), name='book_update'),
    path('book_delete/<int:pk>/', DeleteBook.as_view(), name='delete_book')
]
