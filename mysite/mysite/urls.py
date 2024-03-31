"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from polls.views import log, register,main_menu, reg, log_in, user_log_out
from polls.profile import profile_info, profile_data
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', log, name='log'),
    path("reg/",reg,name='reg'),
    path("main/",main_menu, name = 'main_menu'),
    path('check/', reg,name="reg"),
    path("register",register, name ='register'),
    path("log_in",log_in,name="log_in"),
    path("user_log_out", user_log_out, name="user_log_out"),
    path("profile/",profile_info, name="profile_info"),
    path("page/", profile_data, name="profile_data")
]

