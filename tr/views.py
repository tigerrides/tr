from django.shortcuts import render
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from login.models import LogInInfo
from django.db.models import Q
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate
# , login
from django.contrib.auth.models import User
from create_ride.models import InputRideInfo
from django.template import Context
from uniauth.decorators import login_required


def createUser(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			new_user.save()
			# login_auto_first=request.POST['username']
			# login_auto_last=request.POST['password']
			# user=authenticate(request, username=login_auto_first, password=login_auto_last)
			# login(request, user)
			return render(request, 'welcome.html')
	else:
		form = UserForm()
	return render(request, 'createUser.html', {'form': form})


def login(request):
	return render(request, 'registration/login.html')

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		return render(request, 'home.html')
    # return HttpResponse("welcome.html")
	return render(request, 'welcome.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
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
	# print("group info")
	# print(ride_id)
	rideId = request.POST.get('rideId', None)
	ridesFiltered = InputRideInfo.objects.filter(group_identifier=rideId).filter(ride_status_open=True).values()
	for ride in ridesFiltered:
		origin = ride['depart_from']
		destination = ride['destination']
		date = ride['date']
		break
	return render(request, 'groupInfo.html', {'rides': ridesFiltered, 'rideId': rideId,
											  'origin': origin, 'destination' : destination,
											  'date': date})

def joinGroup(request):
	# print("join group")
	# print(my_ride_id)
	all_my_rides = InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=True).values()
	my_last_ride = all_my_rides.order_by('created').last()
	my_last_ride_id = my_last_ride['group_identifier']
	rideId = request.POST.get('rideId', None)
	save_details = model_to_dict(InputRideInfo.objects.get(group_identifier=my_last_ride_id))
	print("save_details")
	print(save_details)
	origin = save_details['depart_from']
	destination = save_details['destination']
	date = save_details['date']
	update_ride = InputRideInfo.objects.filter(group_identifier=my_last_ride_id).update(group_identifier=rideId)
	print("adding myself to the group")
	print(update_ride)
	ridesFiltered = InputRideInfo.objects.filter(group_identifier=rideId).filter(ride_status_open=True).values()
	print(ridesFiltered)

	return render(request, 'joinGroup.html', {'rides_filt': ridesFiltered, 'single_ride': save_details,
											  'origin': origin, 'destination' : destination,
											  'date': date})

def rideHistory(request):
	open_rides = InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=True).values()
	closed_rides = InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=False).values()
	open_rides_dict = {}
	closed_rides_dict = {}
	for ride in open_rides:
		group_id = ride['group_identifier']
		open_rides_dict[group_id] = InputRideInfo.objects.filter(group_identifier=group_id).values()
		# open_rides_dict[ride.id] = InputRideInfo.objects.filter(id=ride.id).values()
	for ride in closed_rides:
		group_id = ride['group_identifier']
		closed_rides_dict[group_id] = InputRideInfo.objects.filter(group_identifier=group_id).values()
		# closed_rides_dict[ride.id] = InputRideInfo.objects.filter(id=ride.id).values()
	all_my_rides = InputRideInfo.objects.filter(user=request.user).values()
	return render(request, 'rideHistory.html', {'open_rides': open_rides_dict,
												'closed_rides': closed_rides_dict})

@login_required
def searchResults(request, ride_id):
	# submitted_ride = model_to_dict(InputRideInfo.objects.all().order_by('created').last())
	submitted_ride = model_to_dict(InputRideInfo.objects.get(group_identifier=ride_id))
	print("is this the right ride_id")
	print(ride_id)
	print("my most recent submitted_ride")
	print(submitted_ride)
	values = InputRideInfo.objects.filter(
		time_start__lte=submitted_ride['time_end']
	).filter(
		time_end__gte=submitted_ride['time_start']
	).filter(depart_from__contains=submitted_ride['depart_from']
			 ).filter(destination__contains=submitted_ride['destination']
					  ).filter(date=submitted_ride['date']
							   ).filter(~Q(user=request.user)
										).filter(ride_status_open=True).values()

	print(values)
	values_dict = {}
	for ride in values:
		# print(ride['id'])
		group_id = ride['group_identifier']
		# if a group with your user already exists
		if InputRideInfo.objects.filter(group_identifier=group_id).filter(user=request.user).exists():
			continue

		# check to make sure all the riders in that group match with you
		count = InputRideInfo.objects.filter(group_identifier=group_id).count()
		count_with_time = InputRideInfo.objects.filter(group_identifier=group_id).filter(
			time_start__lte=submitted_ride['time_end']
		).filter(
			time_end__gte=submitted_ride['time_start']
		).count()
		if count != count_with_time:
			continue

		# groups
		values_dict[group_id] = InputRideInfo.objects.filter(group_identifier=group_id).values()

	print(values_dict)
	return render(request, 'searchResults.html', {'rides': values_dict, 'my_ride_id': ride_id})

	# return render(request, 'searchResults.html', {'rides': values})

def newRide(request):
	return render(request, 'newride.html')

def completeRide(request):
	return render(request, 'completeRide.html')
