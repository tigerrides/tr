from django.db import models
# from models.utils import Choices

# Create your models here.
class InputRideInfo(models.Model):
    # ewr = "EWR"
    # phl = "PHL"
    # jfk = "JFK"
    # campus = "PRINCETON"
    # depart_from = (
    #     (ewr, "ewr"),
    #     (phl, "phl"),
    #     (jfk, "jfk"),
    #     (campus, "princeton")
    # )
    # destination = (
    #     (ewr, "ewr"),
    #     (phl, "phl"),
    #     (jfk, "jfk"),
    #     (campus, "princeton")
    # )
    # drop down menu
    # depart_from = Choices('ewr', 'phl', 'jfk', 'princeton')
    # destination = Choices('ewr', 'phl', 'jfk', 'princeton')
    date = models.DateField()
    # not sure what auto_now and auto_now_add means
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)
    notes = models.CharField(max_length=500)
    #check boxes
    uber = models.BooleanField(default=False)
    lyft = models.BooleanField(default=False)
    # img = models.ImageField(default='default.png', blank=True)

    # def __str__(self):
        # return '%s %s %s' % (self.first_name, self.last_name, self.phone_number)