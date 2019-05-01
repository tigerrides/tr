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
    from django.forms.models import model_to_dict
    # submitted_ride = model_to_dict(InputRideInfo.objects.latest('created'))
    submitted_ride = model_to_dict(InputRideInfo.objects.order_by('created')).last()
    print("submitted_ride")
    print(submitted_ride)

    print("all rides")
    print(list(InputRideInfo.objects.values()))

    import datetime as dt
    from datetime import timedelta
    # maybe have these ranges be customizable? but for now, add one hour pad

    delta = timedelta(hours=1)
    values = list(InputRideInfo.objects.filter(
        time_start__range=((dt.datetime.combine(dt.date(1,1,1), submitted_ride['time_start'])
            - timedelta(hours=1)).time(), (dt.datetime.combine(dt.date(1,1,1), submitted_ride['time_start'])
            + timedelta(hours=1)).time())
        ).filter(time_end__range=((dt.datetime.combine(dt.date(1,1,1), submitted_ride['time_end'])
            - timedelta(hours=1)).time(), (dt.datetime.combine(dt.date(1,1,1), submitted_ride['time_end'])
            + timedelta(hours=1)).time())
            ).filter(depart_from__contains=submitted_ride['depart_from']
                ).filter(destination__contains=submitted_ride['destination']
                    ).filter(date=submitted_ride['date']).values())
    print(values)

    # values() returns a QuerySet, so turn it into a list, and 
    # turn the list into a dict by iterating over the list and assigning
    # integers as keys (these corresond with 'id' field in each RideInfo
    # model but haven't figured out how to get them in yet, python doesn't
    # like having a dict in the index spot
    values_dict = {}
    ride_count = 1
    for ride in values:
        values_dict[ride_count] = ride
        ride_count += 1

    print(values_dict)

    return render(request, 'searchResults.html', {"rides": values_dict})

    #return render(request, 'searchResults.html', {"rides": {
    #    "ride1": {'depart_from': 'ewr', 'destination': 'princeton', 'date': 'dean\'s date', 'time_start': '6am,', 'time_end': '7am'},
    #    "ride2": {'depart_from': 'princeton', 'destination': 'jfk', 'date': 'princetoween', 'time_start': '8am', 'time_end': '9am'},
    #    "ride3": {'depart_from': 'princeton', 'destination': 'phl', 'date': 'dranksgiving', 'time_start': '6pm', 'time_end': '8pm'},
    #    }})

def newRide(request):
	return render(request, 'newride.html')
