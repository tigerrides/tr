from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class UserForm(ModelForm):
	model = User
	fields = ('username', 'email', 'password')