from django.shortcuts import render
from create_ride.models import InputRideInfo

def groupInfo(request, id):
    print("group info")
    print(id)
    rideId = request.POST.get('rideId', None)
    ridesFiltered = InputRideInfo.objects.filter(group_identifier=rideId).filter(ride_status_open=True).values()
    return render(request, 'groupInfo.html', {'rides': ridesFiltered, 'rideId': rideId})
