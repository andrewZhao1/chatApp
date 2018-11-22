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
	user = models.user.objects.get(phone_number=phone)
	if user and user.password == password:
		return render(request, 'chatApp/main.html', {'user': user})
	else:
		return render(request, 'chatApp/index.html', {'message': '用户不存在或密码错误'})



def register_action(request):
	userid = request.POST.get('userid')
	name = request.POST.get('name')
	phone = request.POST.get('phone')
	password = request.POST.get('password')
	age = request.POST.get('age')
	birthday = request.POST.get('birthday', 'null')
	
	if userid == '0':
		models.user.objects.create(user_name=name, phone_number=phone, password=password, age=age, birthday=birthday)
		return render(request, 'chatApp/index.html')
	else:
		user = models.user.objects.get(pk=userid)
		user.user_name = name
		user.phone_number = phone
		user.password = password
		user.age = age
		user.birthday = birthday
		user.save()
		return render(request, 'chatApp/main.html', {'user': user})