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
        form = forms.CreateRide(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            if LogInInfo.objects.filter(user=request.user).exists():
                get_info = LogInInfo.objects.get(user=request.user)
                instance.user_first_name = get_info.first_name
                instance.user_last_name = get_info.last_name
            instance.user = request.user
            instance.save()
            print("saved")
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

class RideListView(generic.ListView):
    model = InputRideInfo
