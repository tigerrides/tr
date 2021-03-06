from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import LogInInfo
from . import forms
from django.contrib.auth.models import User
# imports for tigerbook api headers
import hashlib
import random
from base64 import b64encode
from datetime import datetime
import requests
import json
# imports needed to get photo from url 
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
import io

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
        
        userName = request.user.username
        arr = userName.split('-')
        netid = arr[2]
        print("netid")
        print(netid)

        form = forms.CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            if LogInInfo.objects.filter(user=request.user).exists():
                LogInInfo.objects.filter(user=request.user).update(
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"],
                    phone_number=request.POST["phone_number"],
                    netid=netid,
                    pic_url="N/A"
                )
                var = LogInInfo.objects.filter(user=request.user).get()
                var.image = form.cleaned_data['image']
                var.save()
            else:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.netid = netid
                instance.pic_url = "N/A"
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
        print("phone number is: " + phone)

    # get netid from user 
    userName = request.user.username
    arr = userName.split('-')
    netid = arr[2]
    print("netid hopefully is: " + arr[2])

    # set up headers for tigerbook api 
    url = 'https://tigerbook.herokuapp.com/api/v1/undergraduates'
    #url = 'https://tigerbook.herokuapp.com/api/aPNwzUMmFu2UtWVMtil8'
    created = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    nonce = ''.join([random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=') for i in range(32)])
    username = 'nbs'
    password = '9194a9a482af7e5bc117c255a7a4d82a'
    generated_digest = b64encode(hashlib.sha256(nonce.encode('utf-8') + created.encode('utf-8') + password.encode('utf-8')).digest()).decode()
    headers = {
        'Authorization': 'WSSE profile="UsernameToken"',
        'X-WSSE': 'UsernameToken Username="%s", PasswordDigest="%s", Nonce="%s", Created="%s"' % (username, generated_digest, b64encode(nonce.encode()).decode(), created)
    }
    # NEEDS NETID
    r = requests.get(url + '/' + netid, headers=headers)
    student = json.loads(r.text)

    # get photos from url
    image_url = student['photo_link']
    # create user
    profile = LogInInfo(
        user=request.user,
        first_name=student['first_name'],
        last_name=student['last_name'],
        phone_number=phone,
        netid=netid,
        pic_url="tigerbook",
        )

    profile.save()

    # none of this works because CAS protects accessing Tigerbook images in this way :(
    # image_url = student['photo_link']
    # print(image_url)
    # img_temp = NamedTemporaryFile()
    # img_temp.write(urlopen(image_url, data=None).read())
    # img_temp.flush()
    # profile.image.save(f"image_{netid}", File(img_temp))
    # profile.save()

    # dummy pic to fill image field
    image_url = "https://campusplan.princeton.edu/sites/campusplan2/files/styles/pwds_media_xxlarge_no_crop/public/banner-2017-campus-plan-28.jpg?itok=QwrGwh5R"
    img_temp = NamedTemporaryFile()
    img_temp.write(urlopen(image_url, data=None).read())
    img_temp.flush()
    profile.image.save(f"tigerbook", File(img_temp))
    profile.save()

    return redirect('currentprof')
