from django.shortcuts import render, redirect, render_to_response
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from login.models import LogInInfo
from django.db.models import Q
from django.http import HttpResponse
from .forms import UserForm
from create_ride.models import InputRideInfo
from django.template import Context
from uniauth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template import RequestContext
from . import settings


def my_custom_page_not_found_view(request, exception):
	return render(request, '404.html', status=404)

def about(request):
	return render(request, 'about.html')

def chooselogin(request):
	return render(request, 'chooseLogin.html')

def completeRide(request):
	rideId = request.POST.get('rideId', None)
	ridesFiltered = InputRideInfo.objects.filter(group_identifier=rideId).filter(ride_status_open=True).values()
	for ride in ridesFiltered:
		origin = ride['depart_from']
		destination = ride['destination']
		date = ride['date']
		break
	return render(request, 'completeRide.html', {'rides': ridesFiltered, 'rideId': rideId,
											  'origin': origin, 'destination' : destination,
											  'date': date})
def contact(request):
	return render(request, 'contact.html')

@login_required
def createRide(request):
	return render(request, 'createRide.html')

@login_required
def createUser(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			new_user.save()
			return render(request, 'welcome.html')
	else:
		form = UserForm()
	return render(request, 'createUser.html', {'form': form})

@login_required
def currentprof(request):
	if LogInInfo.objects.filter(user=request.user).exists():
		# save login info of the current authenticated user if he exists
		login_infos = LogInInfo.objects.filter(user=request.user)
		# number of rides the user has completed
		number_of_rides_completed = InputRideInfo.objects.filter(user=request.user).filter(ride_status_open=False).count()
		return render(request, 'currentprof.html', {'login_infos': login_infos,
													'rides_comp': number_of_rides_completed})
	# if current user's login info doesn't exist, tell him/her to make one
	else:
		return render(request, 'chooseLogin.html')

def deleteRide(request):
	rideId = request.POST.get('rideId', None)
	print("rideId")
	ridesFiltered = InputRideInfo.objects.filter(group_identifier=rideId).filter(ride_status_open=True).values()
	for ride in ridesFiltered:
		origin = ride['depart_from']
		destination = ride['destination']
		date = ride['date']
		break
	return render(request, 'deleteRide.html', {'rides': ridesFiltered, 'rideId': rideId,
											   'origin': origin, 'destination' : destination, 'date': date})
@login_required
def groupInfo(request):
	rideId = request.POST.get('rideId', None)
	if InputRideInfo.objects.filter(group_identifier=rideId).count() == 0:
		return render(request, 'joinGroup2.html')
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
def home(request):
	if LogInInfo.objects.filter(user=request.user).exists():
		return render(request, 'home.html')
	else:
		return render(request, 'chooseLogin.html')
	# return render(request, 'home.html')

# Create your views here.
def index(request):
	if request.user.is_authenticated:
		return render(request, 'home.html')
	# return HttpResponse("welcome.html")
	return render(request, 'welcome.html')

@login_required
def join(request, ride_id):
	my_last_ride_id = ride_id
	rideId = request.POST.get('rideId', None)
	try:
		InputRideInfo.objects.get(group_identifier=my_last_ride_id)
	except InputRideInfo.MultipleObjectsReturned:
		return render(request, 'joinGroup2.html')
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

	subject = 'TigerRide Group for %s' % date
	message = 'Dear TigerRider, \n\n' \
			  'Your trip is scheduled from %s to %s on %s. \n\n' \
			  'Safe travels! \n\n' \
			  'TigerRide' % (origin, destination, date)
	email_from = settings.EMAIL_HOST_USER
	recipient_list = []
	for rides in ridesFiltered:
		netid = rides['netid']
		email = netid + '@princeton.edu'
		recipient_list.append(email)
	send_mail(subject, message, email_from, recipient_list)

	return render(request, 'joinGroup.html', {'rides_filt': ridesFiltered, 'single_ride': save_details,
											  'origin': origin, 'destination' : destination,
											  'date': date})

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

@login_required
def login(request):
	if LogInInfo.objects.filter(user=request.user).exists():
		return render(request, 'home.html')
	else:
		return render(request, 'chooseLogin.html')

@login_required
def newRide(request):
	return render(request, 'newride.html')

def reloadRideHistory(request, which_one):
	no = InputRideInfo.objects.count()
	val = 0
	if no == 0:
		val = 1
	else:
		get_highest = InputRideInfo.objects.all().order_by('group_identifier').last()
		val = get_highest.group_identifier + 1
	rideId = request.POST.get('rideId', None)
	# complete ride
	if which_one == 1:
		InputRideInfo.objects.filter(group_identifier=rideId).filter(user=request.user).update(ride_status_open=False)
	# leave ride
	elif which_one == 2:
		my_ride = InputRideInfo.objects.filter(group_identifier=rideId).filter(user=request.user).values()
		print("my ride")
		print(my_ride)
		for ride in my_ride:
			id = ride['id']
			me_fn = ride['user_first_name']
			me_ln = ride['user_last_name']
		InputRideInfo.objects.filter(id=id).update(group_identifier=val)
		other_riders = InputRideInfo.objects.filter(group_identifier=rideId).values()
		subject = 'TigerRide Trip Update'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = []
		for rides in other_riders:
			netid = rides['netid']
			email = netid + '@princeton.edu'
			recipient_list.append(email)
			origin = rides['depart_from']
			destination = rides['destination']
			date = rides['date']
		message = 'Dear TigerRider, \n\n' \
				  '%s %s has left your group for your trip scheduled from %s to %s on %s. \n\n' \
				  'Safe travels! \n\n' \
				  'TigerRide' % (me_fn, me_ln, origin, destination, date)
		send_mail(subject, message, email_from, recipient_list)
	# delete ride
	elif which_one == 3:
		InputRideInfo.objects.filter(group_identifier=rideId).filter(user=request.user).delete()

	return redirect('rideHistory')

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
	return render(request, 'rideHistory.html', {'open_rides': open_rides_dict,
							'closed_rides': closed_rides_dict, 'open_sing': open_info_singular,
							'closed_sing': close_info_singular})

@login_required
def searchResults(request, ride_id):
	# if a rider already simultaneously matched with them
	try:
		submitted_ride = model_to_dict(InputRideInfo.objects.get(group_identifier=ride_id))
	except InputRideInfo.MultipleObjectsReturned:
		return render(request, 'joinGroup2.html')
	except InputRideInfo.DoesNotExist:
		return render(request, 'joinGroup2.html')

	# filter all the InputRideInfo objects that are open rides and overlap with
	# your time, have the same origin, destination, and date
	values = InputRideInfo.objects.filter(
		time_start__lte=submitted_ride['time_end']
	).filter(time_end__gte=submitted_ride['time_start']
			 ).filter(depart_from__contains=submitted_ride['depart_from']
					  ).filter(destination__contains=submitted_ride['destination']
							   ).filter(date=submitted_ride['date']
										).filter(ride_status_open=True).values()
	# if no objects return, tell the user that no riders match with them
	if not values:
		return render(request, 'searchResultsEmpty.html')
	# dictionary that organizes the group, where the key is the id of the group,
	# and value are the filtered InputRideInfo objects
	groups_dict = {}
	# need this to be able to render origin, destination, date only once...
	ride_info_per_ride = {}
	for ride in values:
		group_id = ride['group_identifier']
		# if the user is already in this group, do not add it to the dictionary
		if InputRideInfo.objects.filter(group_identifier=group_id).filter(user=request.user).exists():
			continue
		# check to make sure all the riders in that group also overlap with your time
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
		groups_dict[group_id] = all_matchings
		for save_ride in all_matchings:
			info_dict['origin'] = save_ride['depart_from']
			info_dict['destination'] = save_ride['destination']
			info_dict['date'] = save_ride['date']
			break
		ride_info_per_ride[group_id] = info_dict
	if not groups_dict:
		return render(request, 'searchResultsEmpty.html')
	return render(request, 'searchResults.html', {'rides': groups_dict, 'my_ride_id': ride_id,
												  'ride_infos': ride_info_per_ride})

@login_required
def seeGroup(request, ride_id):
	rideId = request.POST.get('rideId', None)
	if InputRideInfo.objects.filter(group_identifier=rideId).count() == 0:
		return render(request, 'joinGroup2.html')
	ridesFiltered = InputRideInfo.objects.filter(group_identifier=rideId).filter(ride_status_open=True).values()
	for ride in ridesFiltered:
		origin = ride['depart_from']
		destination = ride['destination']
		date = ride['date']
		break
	return render(request, 'groupInfo.html', {'rides': ridesFiltered, 'rideId': rideId,
											  'origin': origin, 'destination' : destination,
											  'date': date, 'my_ride_id': ride_id})

@login_required
def userProf(request):
	usernet = request.POST.get('userNetid', None)
	print(usernet)
	login_infos = LogInInfo.objects.filter(netid=usernet)
	number_of_rides_completed = InputRideInfo.objects.filter(netid=usernet).filter(ride_status_open=False).count()
	return render(request, 'userProf.html', {'login_infos': login_infos, 'rides_comp': number_of_rides_completed})

def welcome(request):
	return render(request, 'welcome.html')
