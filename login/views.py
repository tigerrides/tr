from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import LogInInfo
from . import forms

# Create your views here.

def index(request):
    return render(request, 'chooseLogin.html')

def createprof(request):
    return render(request, 'createprof.html')

def profile_create(request):

    if request.method == 'POST':
        print("it works!")

        # user = None
        if not request.user.is_authenticated():
            raise Http404
            # user = request.user.username
            # user = request.user.get_username()
        # validate info against form
        # user = request.user
        # first_name = request.POST["first_name"]
        # last_name = request.POST["last_name"]
        # phone_number = request.POST["phone_number"]
        # # img = request.POST["img"]
        # profile_info = LogInInfo(user=user,
        #                          first_name=first_name,
        #                          last_name=last_name,
        #                          phone_number=phone_number,
        #                          )
        #
        # profile_info.save()
        form = forms.CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        #     # save prof to db
        return redirect('home')
    else:
        form = forms.CreateProfile()
    return render(request, 'createprof.html', {'form': form})
