from django.urls import path
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='chooselogin'),
    path('createprof/', views.createprof, name='createprof'),
    path('createprof/profile_create/', views.profile_create, name='profile_create'),
    path('cascreateprof', views.cascreateprof, name='cascreateprof'),
    path('cascreateprof/cas_profile_create/', views.cas_profile_create, name='cas_profile_create')
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]