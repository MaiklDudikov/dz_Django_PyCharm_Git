from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_task, name='list_task'),
    path('login/', views.login_view, name='login'),
    path('calculate/', views.calculate_view, name='calculate'),
    path('register/', views.register_view, name='register'),
    path('programmer-day/', views.programmer_day_view, name='programmer_day'),
]
