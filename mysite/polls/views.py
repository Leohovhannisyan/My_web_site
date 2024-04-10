from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import FriendFusionUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from .group import  Group

def log(request):
    return render(request, 'log_in.html')
def reg(request):
    return render(request, 'register.html')

def main_menu(request):
    user_first_name = request.session.get('user_name')
    user = User.objects.get(username=user_first_name)
    poll_user = FriendFusionUser.objects.get(user=user)
    user_image = None
    try:
        img = FriendFusionUser.objects.get(user=User.objects.get(username=user_first_name))
        user_image = img.user_image
    except FriendFusionUser.DoesNotExist:
        pass
    groups = Group.objects.filter(admins=poll_user)
    context = {
        "user_first_name": user_first_name,
        "user_image": user_image,
        "groups": groups
    }
 
    return render(request, 'main_menu.html', context)







