from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
	# users = models.user.objects.all
	return render(request, 'chatApp/index.html')

def register(request):
	return render(request, 'chatApp/register.html')

def login_action(request):
	phone = request.POST.get('phone')
	password = request.POST.get('password')
	user = models.user.objects.get(userPhoneNum=phone)
	if user and user.userPw == password:
		return render(request, 'chatApp/main.html', {'user':user})
	else:
		return render(request, 'chatApp/index.html', {'message':'用户不存在或密码错误'})



def register_action(request):
	name = request.POST.get('name')
	phone = request.POST.get('phone')
	password = request.POST.get('password')
	age = request.POST.get('age')
	models.user.objects.create(userName=name, userPhoneNum=phone, userPw=password, userAge=age)
	return render(request, 'chatApp/index.html')