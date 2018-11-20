from django.urls import path
from . import views

app_name = '[chatApp]'
urlpatterns = [
    path('index/', views.index),
    path('register/', views.register, name='register'),
]
