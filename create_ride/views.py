from django.shortcuts import render, redirect
from .models import InputRideInfo
from . import forms

# Create your views here.
def rides(request):
    # print("hi")
    return render(request, 'createRide.html')
    # return render(request, 'home.html')

def see_Rides(request):
    data = InputRideInfo.objects.all()
    rides_list = {
        "ride_number": data
    }
    return render(request, 'searchResults.html', rides_list)

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
        uber = request.POST.get('uber', False)
        lyft = request.POST.get('lyft', False)

        if uber != False:
            uber = True

        if lyft != False:
            lyft = True

        # phone_number = request.POST["phone_number"]
        # img = request.POST["img"]
        input_ride_info = InputRideInfo(
                                        depart_from=depart_from,
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
        return redirect('searchResults')
    else:
        form = forms.CreateRide()
    return render(request, 'createRide.html', {'form': form})

# def searchResults(request):
#     return render(request, 'home.html')
