from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('createprof/', views.createprof, name='createprof'),
    path('createprof/profile_create/', views.profile_create, name='profile_create')
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
]