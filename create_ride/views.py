from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

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
    if request.method == 'POST':
        # print("it works!")
        # validate info against form
        if not request.user.is_authenticated:
            raise Http404

        no = InputRideInfo.objects.count()
        val = 0
        if no == None:
            val = 1
        else:
            val = no + 1

        depart_from = request.POST["depart_from"]
        destination = request.POST["destination"]
        date = request.POST["date"]
        time_start = request.POST["time_start"]
        time_end = request.POST["time_end"]
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

        return redirect('searchResults')
    else:
        form = forms.CreateRide()
    return render(request, 'createRide.html', {'form': form})

# def searchResults(request):
#     return render(request, 'home.html')

class RideListView(generic.ListView):
    model = InputRideInfo
