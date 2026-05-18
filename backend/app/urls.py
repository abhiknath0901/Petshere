from django.urls import path

from .views import get_pets
urlpatterns = [
    path('pets/', get_pets, name='get_pets'),
]

