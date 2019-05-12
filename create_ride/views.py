from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime

from .models import InputRideInfo
from login.models import LogInInfo
from . import forms
from django.views import generic
# Create your views here.
def rides(request):
    # print("hi")
    return render(request, 'createRide.html')
    # return render(request, 'home.html')

def see_Rides(request):
    #data = InputRideInfo.objects.all()
    #rides_list = {
    #    "ride_number": data
    #}
    #return render(request, 'searchResults.html', rides_list)
    import datetime
    html = "<html><body>It is now %s.</body></html>" % datetime.datetime.now()
    return HttpResponse(html)

def submit_ride(request):
    form = forms.CreateRide()
    if request.method == 'POST':
        # print("it works!")
        # validate info against form
        if not request.user.is_authenticated:
            raise Http404

        no = InputRideInfo.objects.count()
        val = 0
        if no == 0:
            val = 1
        else:
            get_highest = InputRideInfo.objects.all().order_by('group_identifier').last()
            val = get_highest.group_identifier + 1

        depart_from = request.POST["depart_from"]
        destination = request.POST["destination"]
        if depart_from == destination:
            message = "you cannot travel to the same place!"
            return render(request, 'createRide.html', {'err_message': message})
        date = request.POST["date"]
        dt_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        if dt_date < datetime.date.today():
            message = "the date cannot be in the past!"
            return render(request, 'createRide.html', {'form': form, 'err_message': message})
        time_start = request.POST["time_start"].time()
        time_end = request.POST["time_end"].time()
        dt_start = datetime.datetime.strptime(time_start, '%H:%M:%S')
        dt_end = datetime.datetime.strptime(time_end, '%H:%M:%S')
        if dt_end < dt_start:
            message = "your departure interval is invalid!"
            return render(request, 'createRide.html', {'form': form, 'err_message': message})
        notes = request.POST["notes"]
        uber = request.POST.get('uber', False)
        lyft = request.POST.get('lyft', False)

        if uber != False:
            uber = True

        if lyft != False:
            lyft = True

        input_ride_info = InputRideInfo(user=request.user,
                                        depart_from=depart_from,
                                        destination=destination,
                                        date=date,
                                        group_identifier=val,
                                        time_start=time_start,
                                        time_end=time_end,
                                        notes=notes,
                                        uber=uber,
                                        lyft=lyft,
                                        )
        input_ride_info.save()

        if LogInInfo.objects.filter(user=request.user).exists():
            get_info = LogInInfo.objects.get(user=request.user)
            input_ride_info.user_first_name = get_info.first_name
            input_ride_info.user_last_name = get_info.last_name
            input_ride_info.netid=get_info.netid

        input_ride_info.save()

        # form = forms.CreateRide(request.POST, request.FILES)
        # if form.is_valid():
        #     instance = form.save(commit=False)
        #     if LogInInfo.objects.filter(user=request.user).exists():
        #         get_info = LogInInfo.objects.get(user=request.user)
        #         instance.user_first_name = get_info.first_name
        #         instance.user_last_name = get_info.last_name
        #     instance.user = request.user
        #     instance.save()
        #     print("saved")
        print("submit_ride")
        print(input_ride_info.group_identifier)
        return redirect('searchResults', ride_id=input_ride_info.group_identifier)
    return render(request, 'createRide.html', {'form': form})

# def searchResults(request):
#     return render(request, 'home.html')

class RideListView(generic.ListView):
    model = InputRideInfo
