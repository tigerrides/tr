from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('createprof/', views.createprof, name='createprof'),
    path('createprof/profile_create/', views.profile_create, name='profile_create')
]