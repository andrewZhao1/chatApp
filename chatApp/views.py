from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
	# users = models.user.objects.all
	return render(request, 'chatApp/index.html')

def register(request):
	return render(request, 'chatApp/register.html')
