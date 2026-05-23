from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.create_user, name='create_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('pets/', views.get_pets, name='get_pets'),
    path('cart/', views.get_cart, name='get_cart'),
    path('cart/sync/', views.sync_cart, name='sync_cart'),
    path("save-address/", views.save_address, name='save_address'),
    path("create-payment/",views.create_payment, name='create-payment'),
    path("confirm-order/",views.confirm_order, name='confirm-order'),
]

