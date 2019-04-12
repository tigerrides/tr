from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def index(request):
    return render(request, 'login.html')

def createprof(request):
    return render(request, 'createprof.html')

def profile_create(request):

    if request.method == 'POST':
        # validate info against form
        form = forms.CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # save prof to db
            return redirect('login')
    else:
        form = forms.CreateProfile()
    return render(request, 'createprof.html', {
        'form': form})