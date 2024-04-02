from django.db import models
from django.contrib import admin
from .user import User

class UserImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_image = models.ImageField(default="defualt img")


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ["id"]
