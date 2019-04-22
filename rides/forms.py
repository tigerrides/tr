from django.forms import ModelForm
from . import models


# Create your models here.
class CreateRide(ModelForm):
    class Meta:
        models = models.InputRideInfo
        fields = [
            'depart_from',
            'destination',
            'date',
            'time_start',
            'time_end',
            'notes',
            'uber',
            'lyft',
            # 'img'
        ]