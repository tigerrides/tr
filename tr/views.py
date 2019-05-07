from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from login.models import LogInInfo
from django.db.models import Q
from django.http import HttpResponse
from .forms import UserForm
from create_ride.models import InputRideInfo
from django.template import Context
from uniauth.decorators import login_required
#?? these two 
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

@login_required
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

@login_required
def login(request):
	if LogInInfo.objects.filter(user=request.user).exists():
		return render(request, 'home.html')
	else:
		return render(request, 'chooseLogin.html')

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		return render(request, 'home.html')
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
	print("number of rides")
	print(InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=False).count())
	# number_of_rides_completed = InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=False).count()
	print("rides comp")
	print(InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=False).count())
	return render(request, 'currentprof.html', {'login_infos': login_infos,
												# 'number_of_rides': number_of_rides_completed
												})
	# login_infos = LogInInfo.objects.filter(user=request.user)

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

@login_required
def createRide(request):
	return render(request, 'createRide.html')

@login_required
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

@login_required
def joinGroup(request):
	# print("join group")
	# print(my_ride_id)
	all_my_rides = InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=True).values()
	my_last_ride = all_my_rides.order_by('created').last()
	my_last_ride_id = my_last_ride['group_identifier']
	rideId = request.POST.get('rideId', None)
	try:
		save_details = model_to_dict(InputRideInfo.objects.get(group_identifier=my_last_ride_id))
	except MultipleObjectsReturned:
		return render(request, 'joinGroup2.html')
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

@login_required
def rideHistory(request):
	open_rides = InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=True).values()
	closed_rides = InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=False).values()
	open_rides_dict = {}
	closed_rides_dict = {}
	open_info_singular = {}
	close_info_singular = {}
	for ride in open_rides:
		group_id = ride['group_identifier']
		info_dict = {}
		all_matchings = InputRideInfo.objects.filter(group_identifier=group_id).values()
		open_rides_dict[group_id] = all_matchings
		for save_ride in all_matchings:
			info_dict['origin'] = save_ride['depart_from']
			info_dict['destination'] = save_ride['destination']
			info_dict['date'] = save_ride['date']
			break
		open_info_singular[group_id] = info_dict
		# open_rides_dict[ride.id] = InputRideInfo.objects.filter(id=ride.id).values()
	for ride in closed_rides:
		group_id = ride['group_identifier']
		info_dict = {}
		all_matchings = InputRideInfo.objects.filter(group_identifier=group_id).values()
		closed_rides_dict[group_id] = all_matchings
		for save_ride in all_matchings:
			info_dict['origin'] = save_ride['depart_from']
			info_dict['destination'] = save_ride['destination']
			info_dict['date'] = save_ride['date']
			break
		close_info_singular[group_id] = info_dict
		# closed_rides_dict[group_id] = InputRideInfo.objects.filter(group_identifier=group_id).values()
		# closed_rides_dict[ride.id] = InputRideInfo.objects.filter(id=ride.id).values()
	all_my_rides = InputRideInfo.objects.filter(user=request.user).values()
	return render(request, 'rideHistory.html', {'open_rides': open_rides_dict,
												'closed_rides': closed_rides_dict, 'open_sing': open_info_singular,
												'closed_sing': close_info_singular})

@login_required
def searchResults(request, ride_id):
	# submitted_ride = model_to_dict(InputRideInfo.objects.all().order_by('created').last())
	try:
		submitted_ride = model_to_dict(InputRideInfo.objects.get(group_identifier=ride_id))
	except MultipleObjectsReturned:
		return render(request, 'joinGroup2.html')

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
	ride_info_per_ride = {}
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
		info_dict = {}
		all_matchings = InputRideInfo.objects.filter(group_identifier=group_id).values()
		values_dict[group_id] = all_matchings
		for save_ride in all_matchings:
			print("origin")
			print(save_ride['depart_from'])
			print("dest")
			print(save_ride['destination'])
			print("date")
			print(save_ride['date'])
			info_dict['origin'] = save_ride['depart_from']
			info_dict['destination'] = save_ride['destination']
			info_dict['date'] = save_ride['date']
			break
		ride_info_per_ride[group_id] = info_dict


	print(values_dict)
	return render(request, 'searchResults.html', {'rides': values_dict, 'my_ride_id': ride_id,
												  'ride_infos': ride_info_per_ride})

	# return render(request, 'searchResults.html', {'rides': values})

@login_required
def newRide(request):
	return render(request, 'newride.html')

def completeRide(request):
	# print("group info")
	# print(ride_id)
	rideId = request.POST.get('rideId', None)
	print("rideId")
	ridesFiltered = InputRideInfo.objects.filter(group_identifier=rideId).filter(ride_status_open=True).values()
	for ride in ridesFiltered:
		origin = ride['depart_from']
		destination = ride['destination']
		date = ride['date']
		break
	return render(request, 'completeRide.html', {'rides': ridesFiltered, 'rideId': rideId,
											  'origin': origin, 'destination' : destination,
											  'date': date})

def reloadRideHistory(request, which_one):
	no = InputRideInfo.objects.count()
	val = 0
	if no == 0:
		val = 1
	else:
		get_highest = InputRideInfo.objects.all().order_by('group_identifier').last()
		val = get_highest.group_identifier + 1
	rideId = request.POST.get('rideId', None)
	print("which one")
	print(which_one)
	if which_one == 1:
		InputRideInfo.objects.filter(group_identifier=rideId).filter(user=request.user).update(ride_status_open=False)
	elif which_one == 2:
		my_ride = InputRideInfo.objects.filter(group_identifier=rideId).filter(user=request.user).values()
		id = my_ride.id
		InputRideInfo.objects.filter(id=id).update(group_identifier=val)
	return redirect('rideHistory')

def leaveRide(request):
	rideId = request.POST.get('rideId', None)
	print("rideId")
	ridesFiltered = InputRideInfo.objects.filter(group_identifier=rideId).filter(ride_status_open=True).values()
	for ride in ridesFiltered:
		origin = ride['depart_from']
		destination = ride['destination']
		date = ride['date']
		break
	return render(request, 'leaveRide.html', {'rides': ridesFiltered, 'rideId': rideId,
                                                 'origin': origin, 'destination' : destination,
                                                 'date': date})

# def completeRide(request):
# 	return render(request, 'completeRide.html')
