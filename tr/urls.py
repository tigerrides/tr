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
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('accounts/', include('django.contrib.auth.urls')),
    re_path('accounts/', include('uniauth.urls.cas_only', namespace='uniauth')),
    path('admin/', admin.site.urls),
    path('chooseLogin/', include('login.urls'), name='chooselogin'),
    path('completeRide/', views.completeRide, name='completeRide'),
    path('contact/', views.contact, name='contact'),
    path('createRide/', include('create_ride.urls'), name='createRide'),
    path('createUser/', views.createUser, name='createUser'),
    path('currentprof/', views.currentprof, name='currentprof'),
    path('deleteRide/', views.deleteRide, name='deleteRide'),
    path('groupInfo/', views.groupInfo, name='groupInfo'),
    path('join/<int:ride_id>/', views.join, name='join'),
    path('leaveRide/', views.leaveRide, name='leaveRide'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    # path('joinGroup/', views.joinGroup, name='joinGroup'),
    path('newride/', views.newRide, name='newRide'),
    path('reloadRideHistory/<int:which_one>/', views.reloadRideHistory, name="reloadRideHistory"),
    path('rideHistory/', views.rideHistory, name='rideHistory'),
    path('searchResults/<int:ride_id>/', views.searchResults, name='searchResults'),
    path('seeGroup/<int:ride_id>/', views.seeGroup, name='seeGroup'),
    path('userProf/', views.userProf, name='userProf'),
    path('welcome/', views.welcome, name='welcome'),
]

handler404 = 'tr.views.my_custom_page_not_found_view'


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


