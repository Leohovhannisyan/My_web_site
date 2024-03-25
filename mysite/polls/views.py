from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import PollUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
# Create your views here.
def log(request):
    return render(request, 'log_in.html')
def reg(request):
    return render(request, 'register.html')
def main_menu(request):
    user_first_name = request.session.get('user_name') 
    return render(request, 'main_menu.html',{"user_first_name": user_first_name})
def register(request):
    if request.method == 'GET':
        return render(request, "register.html")

    else:
        username = request.POST["username"]
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        user.first_name = username
        user.save()
        PollUser(user=user).save()

        return HttpResponseRedirect("/main/",)


def log_in(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            request.session['user_name'] = user.first_name
            return redirect('main_menu')

        else:
            return render(request, 'log_in.html')

def user_log_out(request):
     if request.method == 'POST':
        logout(request)
        return render(request,'log_in.html')
