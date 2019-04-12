from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("")

def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    return render(request, 'login.html')

def currentprof(request):
    return render(request, 'currentprof.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')