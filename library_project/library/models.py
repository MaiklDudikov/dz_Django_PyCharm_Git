from django.db import models
from django.contrib.auth.models import User


# Модель книги
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    author = models.CharField(max_length=100, verbose_name="Автор")
    year = models.IntegerField(verbose_name="Год издания")
    style = models.CharField(max_length=50, verbose_name="Стиль")
    publisher = models.CharField(max_length=100, verbose_name="Издательство")
    available = models.BooleanField(default=True, verbose_name="В наличии")

    def __str__(self):
        return self.title


# Модель читателя
class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(verbose_name="E-mail")
    join_date = models.DateField(auto_now_add=True, verbose_name="Дата приёма в библиотеку")
    borrowed_books = models.ManyToManyField(Book, blank=True, verbose_name="Взятые книги")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

