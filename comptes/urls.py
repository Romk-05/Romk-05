from django.urls import path
from .views import inscription_view, connexion_view

urlpatterns = [
    path('inscription/', inscription_view, name='inscription'),
    path('connexion/', connexion_view, name='connexion'),
]