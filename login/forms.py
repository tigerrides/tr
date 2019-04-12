from django.forms import ModelForm
from . import models


# Create your models here.
class CreateProfile(ModelForm):
    class Meta:
        models = models.LogInInfo
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            # 'img'
        ]