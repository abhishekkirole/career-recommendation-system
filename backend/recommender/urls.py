from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('careers/', views.get_all_careers, name='get_all_careers'),
    path('recommendations/', views.get_recommendations, name='get_recommendations'),
    path('auth/register/', views.register_user, name='register_user'),
]