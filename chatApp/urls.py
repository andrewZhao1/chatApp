from django.urls import path
from . import views

app_name = '[chatApp]'
urlpatterns = [
    path('index/', views.index),
    path('register/', views.register, name='register'),
    path('register/action', views.register_action, name='register_action'),
    path('index/login', views.login_action, name='login_action'),
]
