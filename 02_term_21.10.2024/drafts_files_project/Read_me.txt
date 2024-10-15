Задание 1 : Создание веб-приложения с несколькими разделами

1) Создайте новый проект Django :

pip install django
django-admin startproject company_project
cd company_project

2) Создайте приложение внутри проекта :

python manage.py startapp main

3) Зарегистрируйте приложение в settings.py :

INSTALLED_APPS = [
    ...
    'main',
]

4) Определите представления (views) для разделов в файле main/views.py :

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

5) Настройте маршруты для всех разделов в main/urls.py :

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]

6) Включите эти маршруты в файл company_project/urls.py :

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

7)