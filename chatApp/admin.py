from django.contrib import admin

from .models import user


class userAdmin(admin.ModelAdmin):
	list_display = ('user_name','age')


admin.site.register(user, userAdmin)
