from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from polls.models import PollUser
from django.shortcuts import redirect
from polls.models import UserImage

def profile_info(request):
    return render(request,'profile.html')


def profile_data(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get("user_name"))
        email = request.POST.get("email")
        age = request.POST.get("age")
        country = request.POST.get("country")
        city = request.POST.get("city")
        user_image = request.FILES.get("image")

        if email and age and country and city != "":
            user.email = email
            puser = PollUser.objects.get(user=user)
            puser.age = age
            puser.country = country
            puser.city = city
            puser.user_image = user_image
            puser.save()
            user.save()


            return render(request, "main_menu.html")
        else:
            return HttpResponseBadRequest("Enter all data")
    else:
        return HttpResponseBadRequest("Invalid request method")