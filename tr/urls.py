"""tr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('createRide/', include('create_ride.urls'), name='createRide'),
    path('login/', include('login.urls'), name='login'),
    # path('login/', views.login, name='login'),
    path('currentprof/', views.currentprof, name='currentprof'),
    path('home/', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('createRide/', views.createRide, name='createRide'),
    path('groupInfo/', views.groupInfo, name='groupInfo'),
    path('joinGroup/', views.joinGroup, name='joinGroup'),
    path('rideHistory/', views.rideHistory, name='rideHistory'),
    path('searchResults/', views.searchResults, name='searchResults'),
    path(r'^see_rides$', include('create_ride.urls'), name='see_rides'),
    path('newride/', views.newRide, name='newRide')
]
