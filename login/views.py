from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import LogInInfo
from . import forms
# imports for tigerbook api headers
import hashlib
import random
from base64 import b64encode
from datetime import datetime
# imports needed to get photo from url 
from django.core.files import File
import os

# Create your views here.

def index(request):
    return render(request, 'chooseLogin.html')

def createprof(request):
    return render(request, 'createprof.html')

def profile_create(request):
    if request.method == 'POST':
        # print("it works!")
        # user = None
        if not request.user.is_authenticated:
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
            if LogInInfo.objects.filter(user=request.user).exists():
                LogInInfo.objects.filter(user=request.user).update(
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    phone_number=request.POST["phone_number"],
                    netid=request.POST["netid"]
                )
                var = LogInInfo.objects.filter(user=request.user).get()
                var.image = form.cleaned_data['image']
                var.save()
            else:
                instance = form.save(commit=False)
                instance.user = request.user
            # check if it's in the database. if so, update the info else, create a new entry
            # login_infos = LogInInfo.objects.filter(user=request.user)
                instance.save()
        #     # save prof to db
        return redirect('currentprof')
    else:
        form = forms.CreateProfile()
    return render(request, 'createprof.html', {'form': form})

def cascreateprof(request):
    return render(request, 'cascreateprof.html')

def cas_profile_create(request):
    if not request.user.is_authenticated:
            raise Http404

    # get phone number from form
    if request.method == 'POST':
        phone = request.POST["phone_number"]

    # get netid from user 
    userName = request.user
    arr = userName.split('-')

    # get password key
    # key = api/v1/getkey/
    key = "8f1ca00610987bcd533f1d067f333b2c"

    # set up headers for tigerbook api 
    url = 'https://tigerbook.herokuapp.com/api/v1/undergraduates/' + arr[2]
    created = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    nonce = ''.join([random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=') for i in range(32)])
    username = 'christyl'
    password = key
    generated_digest = b64encode(hashlib.sha256(str(nonce) + str(created) + str(password)).digest())
    headers = {
    'Authorization': 'WSSE profile="UsernameToken"',
    'X-WSSE': 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % (username, generated_digest, b64encode(nonce), created)
    }

    # create user
    profile = LogInInfo(
        first_name="first",
        last_name="last",
        phone_number=phone,
        netid=arr[2]
        )
        # get photos from url 
    image_url = https://www.princeton.edu/sites/default/files/styles/full_2x/public/images/2019/05/20190502_GoggleAI_DJA_044_2.jpg?itok=gsOp52yp
    result = urllib.urlretrieve(image_url)
    profile.image.save(
        os.path.basename(image_url),
        File(open(result[0])))
    profile.save();
