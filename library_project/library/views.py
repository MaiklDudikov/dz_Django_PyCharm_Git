from django.shortcuts import render
from .models import Book, Reader


# Отображение всех книг
def all_books(request):
    books = Book.objects.all()
    return render(request, 'library/all_books.html', {'books': books})


# Отображение книг в наличии
def available_books(request):
    books = Book.objects.filter(available=True)
    return render(request, 'library/available_books.html', {'books': books})


# Отображение информации о читателях
def all_readers(request):
    readers = Reader.objects.all()
    return render(request, 'library/all_readers.html', {'readers': readers})
