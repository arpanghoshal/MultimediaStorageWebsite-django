"""cloudproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url

from cloud import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^photos$', views.photos, name='photos'),
    url('^logout$', views.logout, name='logout'),
    url('^checkuser$', views.checkuser, name='checkuser'),
    url('^audios$', views.audios, name='audios'),
    url('^videos$', views.videos, name='videos'),
    url('^upload$', views.addphoto1, name='addphoto1'),
    url('^ap$', views.ap, name='ap'),
    url('^addaudio$', views.addaudio1, name='addaudio'),
    url('^aa$', views.aa, name='aa'),
    url('^addvideo$', views.addvideo1, name='addvideo'),
    url('^av$', views.av, name='av'),
    url('^register$', views.register, name='register'),
    url('^regs$', views.regs, name='regs'),
    url('^login$', views.login, name='login'),
    url('^search$', views.search1, name='search'),


]
