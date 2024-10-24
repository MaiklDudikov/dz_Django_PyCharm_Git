from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurant_list'),
    path('add/', views.add_restaurant, name='add_restaurant'),
    path('<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('<int:pk>/edit/', views.edit_restaurant, name='restaurant_edit'),
    path('<int:pk>/delete/', views.delete_restaurant, name='restaurant_delete'),
    path('search/', views.search_restaurants, name='search_restaurants'),
]
