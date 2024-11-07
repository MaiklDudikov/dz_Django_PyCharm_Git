from django.urls import path
from . import views

urlpatterns = [
    path('', views.favorite_song, name='favorite_song'),
    path('', views.song_in_language, {'lang': 'en'}, name='favorite_song'),
    path('<str:lang>/', views.song_in_language, name='song_in_language'),
]
