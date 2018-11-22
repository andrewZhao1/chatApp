from django.db import models

class user(models.Model):
	phone_number = models.CharField(max_length = 13,unique=True)
	user_name = models.CharField(max_length = 16)
	password = models.CharField(max_length = 16)
	age = models.IntegerField(null=True)
	birthday = models.DateField(null=True)
	create_time = models.DateTimeField(null=True,auto_now_add=True)
	update_time = models.DateTimeField(null=True,auto_now=True)

	def __str__(self):
		return 	self.name
