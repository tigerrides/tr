from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from login.models import LogInInfo
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from create_ride.models import InputRideInfo
from django.template import Context

def createUser(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			# login(request)
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

@login_required
def home(request):
    return render(request, 'home.html')

def welcome(request):
    return render(request, 'welcome.html')

def chooselogin(request):
    return render(request, 'chooseLogin.html')

@login_required
def currentprof(request):
	login_infos = LogInInfo.objects.filter(user=request.user)
	return render(request, 'currentprof.html', {'login_infos': login_infos})
	# login_infos = LogInInfo.objects.filter(user=request.user)

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
    ride_dict = {}

    ride_dict['depart_from'] = 'ewr'
    ride_dict['destination'] = 'princeton'
    ride_dict['date'] = 'this_date'
    ride_dict['time_start'] = 'start-time'
    ride_dict['time_end'] = 'end-time'

    return render(request, 'searchResults.html', context={'ride': ride_dict})

def newRide(request):
	return render(request, 'newride.html')
