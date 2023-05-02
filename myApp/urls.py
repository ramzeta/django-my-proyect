from django.urls import path
from myApp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login_view'),
    path('password_change_done/', views.password_change_done, name='password_change_done'),
    path('password_change_form/', views.password_change_form, name='password_change_form'),
    path('logged_out/', views.logged_out, name='login'),
    path('iris_delete/', views.iris_delete, name='iris_delete'),
    path('iris_insert/', views.iris_insert, name='iris_insert'),
    path('iris_main/', views.iris_main, name='iris_main'),
    path('iris_update/', views.iris_update, name='iris_update'),
]
