from django.urls import path
from .views import ServerTimeView, GreetingView
from . import views

urlpatterns = [
    path('server-info/', ServerTimeView.as_view(), name='server_info'),
    path('greet/', GreetingView.as_view(), name='greet'),
    path('arithmetic/', views.arithmetic_operations, name='arithmetic_operations'),
    path('power/', views.power_operation, name='power_operation'),
]
