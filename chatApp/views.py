from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
	# users = models.user.objects.all
	return render(request, 'chatApp/index.html')

def register(request, userid):
	if str(userid) == '0':
		return render(request, 'chatApp/register.html')
	user = models.user.objects.get(pk=userid)
	return render(request, 'chatApp/register.html', {'user': user})

def login_action(request):
	phone = request.POST.get('phone')
	password = request.POST.get('password')
	user = models.user.objects.get(userPhoneNum=phone)
	if user and user.userPw == password:
		return render(request, 'chatApp/main.html', {'user': user})
	else:
		return render(request, 'chatApp/index.html', {'message': '用户不存在或密码错误'})



def register_action(request):
	userid = request.POST.get('userid')
	name = request.POST.get('name')
	phone = request.POST.get('phone')
	password = request.POST.get('password')
	age = request.POST.get('age')
	
	if userid == '0':
		models.user.objects.create(userName=name, userPhoneNum=phone, userPw=password, userAge=age)
		return render(request, 'chatApp/index.html')
	else:
		user = models.user.objects.get(pk=userid)
		user.userName = name
		user.userPhoneNum = phone
		user.userPw = password
		user.userAge = age
		user.save()
		return render(request, 'chatApp/main.html', {'user': user})