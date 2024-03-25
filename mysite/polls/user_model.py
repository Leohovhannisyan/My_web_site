from django.db import models

from django.contrib.auth.models import User
from django.contrib import admin

class PollUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    


    def __str__(self):
        return "{} ".format(self.user.first_name, self.user.email)

@admin.register(PollUser)
class PollUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_user_info']

    def get_user_info(self, obj):
        return "{} ".format(obj.user.first_name)
    get_user_info.short_description = 'User'
