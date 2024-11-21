from django.urls import path
from .views import PredictionView
from . import views

urlpatterns = [
    path('', PredictionView.as_view(), name='prediction'),
    path('random/', views.random_number, name='random_number'),
    path('random/range/', views.random_number_in_range, name='random_number_in_range'),
    path('random/set/', views.random_number_set, name='random_number_set'),
    path('poem/random/', views.random_poem, name='random_poem'),
    path('poem/author/', views.random_poem_by_author, name='random_poem_by_author'),
    path('poem/theme/', views.random_poem_by_theme, name='random_poem_by_theme'),
    path('poem/titles/author/', views.list_poems_by_author, name='list_poems_by_author'),
    path('poem/authors/', views.list_authors, name='list_authors'),
    path('poem/themes/', views.list_themes, name='list_themes'),
    path('poem/titles/theme/', views.list_poems_by_theme, name='list_poems_by_theme'),
]
