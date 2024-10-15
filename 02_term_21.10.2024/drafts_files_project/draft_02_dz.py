# pip install django - если надо ! ! !
# django-admin startproject company_project
# cd company_project

"""
INSTALLED_APPS = [
    'main',
]



from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def news(request):
    return render(request, 'main/news.html')

def management(request):
    return render(request, 'main/management.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]



from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]



def news(request, extra=None):
    return render(request, 'main/news.html')

def management(request, extra=None):
    return render(request, 'main/management.html')



urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/<str:extra>/', views.news, name='news_extra'),  # Обработка дополнительных URL
    path('management/', views.management, name='management'),
    path('management/<str:extra>/', views.management, name='management_extra'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]


def branches(request, branch=None):
    if branch == 'London':
        return render(request, 'main/branches_london.html')
    elif branch == 'Paris':
        return render(request, 'main/branches_paris.html')
    else:
        return render(request, 'main/branches.html')


urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/<str:extra>/', views.news, name='news_extra'),
    path('management/', views.management, name='management'),
    path('management/<str:extra>/', views.management, name='management_extra'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('branches/', views.branches, name='branches'),
    path('branches/<str:branch>/', views.branches, name='branch'),
]


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Главная</title>
</head>
<body>
    <h1>Главная страница</h1>
    <ul>
        <li><a href="{% url 'news' %}">Новости</a></li>
        <li><a href="{% url 'management' %}">Руководство</a></li>
        <li><a href="{% url 'about' %}">О компании</a></li>
        <li><a href="{% url 'contacts' %}">Контакты</a></li>
        <li><a href="{% url 'branches' %}">Филиалы</a></li>
    </ul>
</body>
</html>


home.html :

<!DOCTYPE html>
<html>
<head>
    <title>Главная</title>
</head>
<body>
    <h1>Главная</h1>
    <p>Добро пожаловать на главную страницу!</p>
    <ul>
        <li><a href="{% url 'news' %}">Новости</a></li>
        <li><a href="{% url 'management' %}">Руководство</a></li>
        <li><a href="{% url 'about' %}">О компании</a></li>
        <li><a href="{% url 'contacts' %}">Контакты</a></li>
        <li><a href="{% url 'branches' %}">Филиалы</a></li>
    </ul>
</body>
</html>


news.html :

<!DOCTYPE html>
<html>
<head>
    <title>Новости</title>
</head>
<body>
    <h1>Новости</h1>
    <p>Последние новости компании.</p>
    <a href="{% url 'home' %}">Назад на главную</a>
</body>
</html>


branches.html :

<!DOCTYPE html>
<html>
<head>
    <title>Филиалы</title>
</head>
<body>
    <h1>Филиалы компании</h1>
    <ul>
        <li><a href="{% url 'branch' 'London' %}">Лондон</a></li>
        <li><a href="{% url 'branch' 'Paris' %}">Париж</a></li>
    </ul>
    <a href="{% url 'home' %}">Назад на главную</a>
</body>
</html>
"""

# python manage.py runserver
# Переходите на различные URL-адреса (например, /news, /branches/London) и проверьте функциональность приложения.
