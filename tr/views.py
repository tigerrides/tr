from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("welcome.html")
	return render(request, 'welcome.html')


def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')

def chooselogin(request):
    return render(request, 'chooseLogin.html')

def currentprof(request):
    return render(request, 'currentprof.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def createRide(request):
	return render(request, 'createRide.html')

def groupInfo(request):
	return render(request, 'groupInfo.html')

def joinGroup(request):
	return render(request, 'joinGroup.html')

def rideHistory(request):
	return render(request, 'rideHistory.html')

def searchResults(request):
	return render(request, 'searchResults.html')

def newRide(request):
	return render(request, 'newride.html')