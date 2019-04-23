from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='createRide'),
    path('rides/submit_ride/', views.submit_ride, name='submit_ride'),
    # path('createprof/profile_create/', views.profile_create, name='profile_create')
]