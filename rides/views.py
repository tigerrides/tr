from django.shortcuts import render
from .models import InputRideInfo
from . import forms

# Create your views here.
def index(request):
    return render(request, 'createRide.html')

def submit_ride(request):
    if request.method == 'POST':
        # print("it works!")
        # validate info against form
        depart_from = request.POST["depart_from"]
        destination = request.POST["destination"]
        date = request.POST["date"]
        time_start = request.POST["time_start"]
        time_end = request.POST["time_end"]
        notes = request.POST["notes"]
        uber = request.POST["uber"]
        lyft = request.POST["lyft"]
        input_ride_info = InputRideInfo(depart_from=depart_from,
                                        destination=destination,
                                        date=date,
                                        time_start=time_start,
                                        time_end=time_end,
                                        notes=notes,
                                        uber=uber,
                                        lyft=lyft,
                                 #phone_number=phone_number,
                                        )
        input_ride_info.save()
        # form = forms.CreateProfile(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     # save prof to db
        return redirect('home')
    else:
        form = forms.CreateRide()
    return render(request, 'createRide.html', {'form': form})