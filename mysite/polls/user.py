from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.utils import timezone
class PollUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default = 0)
    country = models.CharField(max_length=120,default="Default country")
    city = models.CharField(max_length=120,default="Default city")
    user_image = models.ImageField(default="default image")
    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.user.email)

@admin.register(PollUser)
class PollUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']

    def user(self, obj):
        return obj.user.username


