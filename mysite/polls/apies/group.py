from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import PollUser
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout
from django.urls import reverse
from polls.models import PollUser
from polls.group import  Group
from django.contrib.auth.models import User, Permission  
def group_menu(request):
    return render(request, "group_menu.html")

def create_group_view(request):
    if request.method == "POST":
        name = request.POST["group_name"]
        admin_name = request.session.get("user_name") 
        user = User.objects.get(username=admin_name)
        admin = PollUser.objects.get(user=user)
        
        group = Group.objects.create(name=name)
        
        group.admins.add(admin)

      
        group.save()

        codenames = ['add_user', 'change_user', 'delete_user']
        permissions = Permission.objects.filter(codename__in=codenames)
        user.user_permissions.set(permissions)
        admin.save()     
        return redirect("main_menu")
  
    return render(request, 'create_group_form.html')
