from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.all_books, name='all_books'),
    path('books/', views.all_books, name='all_books'),
    path('books/available/', views.available_books, name='available_books'),
    path('readers/', views.all_readers, name='all_readers'),
    path('login/', LoginView.as_view(template_name='library/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('books/filter/', views.books_filter, name='books_filter'),
]
