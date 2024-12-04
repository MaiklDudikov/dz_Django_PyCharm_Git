from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.all_books, name='all_books'),
    path('books/available/', views.available_books, name='available_books'),
    path('readers/', views.all_readers, name='all_readers'),
]
