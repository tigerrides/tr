from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('createprof/', views.createprof, name='createprof'),
]