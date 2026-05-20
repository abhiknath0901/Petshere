from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.create_user, name='create_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('pets/', views.get_pets, name='get_pets'),
    path('cart/<int:user_id>/', views.get_cart, name='get_cart'),
    path('cart/add/<int:user_id>/<int:pet_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:user_id>/<int:pet_id>/', views.remove_from_cart, name='remove_from_cart'),

]

