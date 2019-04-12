from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'login.html')

def createprof(request):
    return render(request, 'createprof.html')