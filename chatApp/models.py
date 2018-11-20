from django.db import models

class user(models.Model):
	userPhoneNum = models.CharField(max_length = 13,null=False)
	userName = models.CharField(max_length = 16,null=False)
	userPw = models.CharField(max_length = 16,null=False)
	userAge = models.IntegerField()

	def __str__(self):
		return 	self.userName
