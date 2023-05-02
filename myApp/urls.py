from django.urls import path
from myApp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # TODO: Añadir las urls para accounts
    # TODO: Añadir las urls para register
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # TODO: Añadir las urls para iris
    # TODO: Añadir las urls para insertData
    # TODO: Añadir las urls para updateData
    # TODO: Añadir las urls para deleteData
]
