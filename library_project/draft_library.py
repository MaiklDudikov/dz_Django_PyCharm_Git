# python manage.py shell
# Выход из shell
# Ctrl + Z и затем Enter (на Windows)

from library.models import Book, Reader
from django.contrib.auth.models import User

# Добавляем книги
books = [
    {"title": "Война и мир", "author": "Лев Толстой", "year": 1869, "style": "Роман", "publisher": "Русский вестник", "available": True},
    {"title": "Преступление и наказание", "author": "Фёдор Достоевский", "year": 1866, "style": "Роман", "publisher": "Русский вестник", "available": True},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков", "year": 1940, "style": "Роман", "publisher": "Современник", "available": True},
    {"title": "Евгений Онегин", "author": "Александр Пушкин", "year": 1833, "style": "Поэма", "publisher": "Северные цветы", "available": True},
    {"title": "Анна Каренина", "author": "Лев Толстой", "year": 1878, "style": "Роман", "publisher": "Русский вестник", "available": False},
    {"title": "Идиот", "author": "Фёдор Достоевский", "year": 1869, "style": "Роман", "publisher": "Русский вестник", "available": True},
    {"title": "Тихий Дон", "author": "Михаил Шолохов", "year": 1940, "style": "Роман", "publisher": "Советский писатель", "available": True},
    {"title": "Отцы и дети", "author": "Иван Тургенев", "year": 1862, "style": "Роман", "publisher": "Русский вестник", "available": False},
    {"title": "Чайка", "author": "Антон Чехов", "year": 1896, "style": "Пьеса", "publisher": "Русская мысль", "available": True},
    {"title": "Горе от ума", "author": "Александр Грибоедов", "year": 1825, "style": "Комедия", "publisher": "Нева", "available": True},
]

for book in books:
    Book.objects.create(**book)

# Создаем пользователей для читателей
users = [
    {"username": "reader1", "password": "password123", "email": "reader1@example.com"},
    {"username": "reader2", "password": "password123", "email": "reader2@example.com"},
    {"username": "reader3", "password": "password123", "email": "reader3@example.com"},
    {"username": "reader4", "password": "password123", "email": "reader4@example.com"},
    {"username": "reader5", "password": "password123", "email": "reader5@example.com"},
]

user_objects = []
for user_data in users:
    user = User.objects.create_user(**user_data)
    user_objects.append(user)

# Добавляем читателей
readers = [
    {"user": user_objects[0], "first_name": "Иван", "last_name": "Иванов", "phone": "123456789", "email": "ivanov@example.com"},
    {"user": user_objects[1], "first_name": "Пётр", "last_name": "Петров", "phone": "987654321", "email": "petrov@example.com"},
    {"user": user_objects[2], "first_name": "Сергей", "last_name": "Сергеев", "phone": "112233445", "email": "sergeev@example.com"},
    {"user": user_objects[3], "first_name": "Мария", "last_name": "Сидорова", "phone": "556677889", "email": "sidorova@example.com"},
    {"user": user_objects[4], "first_name": "Анна", "last_name": "Кузнецова", "phone": "998877665", "email": "kuznetsova@example.com"},
]

for reader in readers:
    Reader.objects.create(**reader)
