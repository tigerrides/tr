from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='createRide'),
    # path('searchResults/', include('create_ride.urls'), name='searchResults'),

    path(r'^searchResults/$', views.see_Rides, name='searchResults'),
    # path('', views.searchResults, name='searchResults'),
    path('rides/submit_ride/', views.submit_ride, name='submit_ride'),
    # path('createprof/profile_create/', views.profile_create, name='profile_create')
]