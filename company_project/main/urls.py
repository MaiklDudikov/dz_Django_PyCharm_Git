from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/<str:extra>/', views.news, name='news_extra'),  # Обработка дополнительных URL
    path('management/', views.management, name='management'),
    path('management/<str:extra>/', views.management, name='management_extra'),  # Обработка дополнительных URL
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('branches/', views.branches, name='branches'),
    path('branches/<str:branch>/', views.branches, name='branch'),  # Обработка дополнительных URL
]
