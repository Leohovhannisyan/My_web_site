from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import PollUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from polls.models import PollUser
from polls.group import  Group


def register(request):
    if request.method == 'GET':
        return render(request, "register.html")

    else:
        first_name = request.POST["name"]
        last_name = request.POST["surname"]
        username = request.POST["username"]
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        PollUser(user=user).save()

        return render(request,"log_in.html")


def log_in(request):
    if request.method == 'GET':
        return render(request, 'log_in.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            request.session['user_name'] = user.username
            return redirect('main_menu')

        else:
            return render(request, 'main_menu.html')

def user_log_out(request):
     if request.method == 'POST':
        logout(request)
        return render(request,'log_in.html')

