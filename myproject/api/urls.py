from django.urls import path
from .views import PredictionView
from . import views

urlpatterns = [
    path('', PredictionView.as_view(), name='prediction'),
    path('random/', views.random_number, name='random_number'),
    path('random/range/', views.random_number_in_range, name='random_number_in_range'),
    path('random/set/', views.random_number_set, name='random_number_set'),
]
