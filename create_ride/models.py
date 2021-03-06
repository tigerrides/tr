from django.db import models
from django.conf import settings

# from models.utils import Choices

# Create your models here.
class InputRideInfo(models.Model): 
    #import datetime
    #time_submitted = datetime.time.now()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=1
    )
    # user_first_name = models.CharField(max_length=20)
    # user_last_name = models.CharField(max_length=20)
    ewr = "EWR"
    phl = "PHL"
    jfk = "JFK"
    p_j = "PRINCETON JUNCTION"
    campus = "PRINCETON"
    ORIGIN_CHOICES = (
        (ewr, "ewr"),
        (phl, "phl"),
        (jfk, "jfk"),
        (p_j, "princeton junction"),
        (campus, "princeton")
    )
    DESTINATION_CHOICES = (
        (ewr, "ewr"),
        (phl, "phl"),
        (jfk, "jfk"),
        (p_j, "princeton junction"),
        (campus, "princeton")
    )
    netid = models.CharField(max_length=200, default="princeton")

    group_identifier = models.IntegerField(default=1)

    approved = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    user_first_name = models.CharField(max_length=200, default="first")
    user_last_name = models.CharField(max_length=200, default="last")
    depart_from = models.CharField(max_length=20, choices=ORIGIN_CHOICES, default=campus)
    destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES, default=campus)

    date = models.DateField()
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)
    notes = models.CharField(max_length=500)
    #check boxes
    uber = models.BooleanField(default=False)
    lyft = models.BooleanField(default=False)
    ride_status_open = models.BooleanField(default=True)


    def __str__(self):
        return '%s %s' % (self.user_first_name, self.user_last_name)

class Ride(models.Model):
    joined_rider = models.ForeignKey(InputRideInfo, on_delete=models.CASCADE)
    ride_status_open = models.BooleanField(default=True)
    #
    # def __str__(self):
    #     return '%s' % (self.joined_rider.user_first_name)
