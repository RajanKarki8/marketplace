from django.urls import path
from . import views

urlpatterns = [
     path('', views.store, name= 'store'),
     path('login/', views.user_login, name = 'login'),
     path('register', views.user_register, name='register'),
     path('logout/', views.user_logout, name = 'logout'),
     path('checkout/', views.checkout, name = 'checkout'),
     path('cart/', views.cart, name = 'cart'),
     
     path('update-item/', views.UpdateItem, name= 'update-item'),
     path('make-order/', views.MakeOrder, name= 'make-order')
     # path('store/', views.store, name = 'store'),
]
