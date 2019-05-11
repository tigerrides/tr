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
    # path('accounts/', include('django.contrib.auth.urls')),
    re_path('accounts/', include('uniauth.urls.cas_only', namespace='uniauth')),
    path('createRide/', include('create_ride.urls'), name='createRide'),
    path('groupInfo/<int:please>/', include('org_rides.urls'), name='what'),
    path('groupInfo/', views.groupInfo, name='groupInfo'),
    path('chooseLogin/', include('login.urls'), name='chooselogin'),
    path('login/', views.login, name='login'),
    path('currentprof/', views.currentprof, name='currentprof'),
    path('home/', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('reloadRideHistory/<int:which_one>/', views.reloadRideHistory, name="reloadRideHistory"),
    # path('createRide/', views.createRide, name='createRide'),
    # path('groupInfo/', views.groupInfo, name='groupInfo'),
    path('joinGroup/', views.joinGroup, name='joinGroup'),
    path('rideHistory/', views.rideHistory, name='rideHistory'),
    path('leaveRide/', views.leaveRide, name='leaveRide'),
    path('deleteRide/', views.deleteRide, name='deleteRide'),
#<<<<<<< HEAD
    #path('searchResults/', views.searchResults, name='searchResults'),
    path(r'^see_rides$', include('create_ride.urls'), name='see_rides'),
    path('newride/', views.newRide, name='newRide'),
    path('searchResults/<int:ride_id>/', views.searchResults, name='searchResults'),
    path('join/<int:ride_id>/', views.join, name='join'),

    # path(r'^searchResults/(?P<int:ride_id>[-\w]+)/$', views.searchResults, name='searchResults'),

         # 'searchResults/', views.searchResults, name='searchResults'),

    # path('searchResults/', views.searchResults, name='searchResults'),
    # path(r'^see_rides$', include('create_ride.urls'), name='see_rides'),
#>>>>>>> 58e80ac679c4a1fe980f2eebabeabb66794c8712
    # path('accounts/login/', include('login.urls'), name='login'),
    path('createUser/', views.createUser, name='createUser'),
    #path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    # path('accounts/logout/', include('login.urls'), name='logout'),
    path('completeRide/', views.completeRide, name='completeRide'),
]

handler404 = 'tr.views.my_custom_page_not_found_view'

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


