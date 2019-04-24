from django.urls import path

from . import views

urlpatterns = [
    path('', views.rides, name='createRide'),
    path('searchResults/', views.searchResults, name='searchResults'),
    path('rides/submit_ride/', views.submit_ride, name='submit_ride'),
    # path('createprof/profile_create/', views.profile_create, name='profile_create')
]