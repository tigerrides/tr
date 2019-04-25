from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User

def createUser(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			#login(request)
			new_user.save()
			return render(request, 'createprof.html')
	else:
		form = UserForm()
	return render(request, 'createUser.html', {'form': form})

def login(request):
	return render(request, 'registration/login.html')

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