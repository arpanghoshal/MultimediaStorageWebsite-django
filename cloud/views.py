import os

from django.shortcuts import render, redirect

from cloud.models import usertable
from cloud.models import addphoto, addvideo, addaudio


def home(request):
    try:
        name = request.session.get('name')
        if name:
            return render(request, 'cloud/home.html', {"name": name})
        else:
            return render(request, 'cloud/home.html')
    except Exception as e:
        print(e)
        return render(request, "cloud/home.html")


def photos(request):
    name = request.session.get('name')
    a = addphoto.objects.all()
    return render(request, 'cloud/photos.html', {"name": name, "a": a})


def audios(request):
    name = request.session.get('name')
    b = addaudio.objects.all()
    return render(request, 'cloud/audios.html', {"name": name, "b": b})


def videos(request):
    name = request.session.get('name')
    c = addvideo.objects.all()
    return render(request, 'cloud/videos.html', {"name": name, "c": c})


def addphoto1(request):
    return render(request, 'cloud/addmedia.html', {})


def ap(request):
    pn = request.POST['photosname']
    pb = request.FILES['photosbrowse']
    extension = os.path.splitext(str(request.FILES['photosbrowse']))[1]
    print()
    ext = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if extension in ext:
        sv = addphoto(photosname=pn, photosbrowse=pb)
        sv.save()
    else:
        print("Enter correct data")

    return render(request, 'cloud/addmedia.html', {})



def addaudio1(request):
    return render(request, 'cloud/addmedia.html', {})


def aa(request):
    an = request.POST['audiosname']
    ab = request.FILES['audiosbrowse']
    extension = os.path.splitext(str(request.FILES['audiosbrowse']))[1]
    ext = ['.mp3', '.mp4', '.wav', '.ogg', '.aac']
    if extension in ext:
        print("Data is saved")
        sv = addaudio(audiosname=an, audiosbrowse=ab)
        sv.save()
    else:
        print("Enter correct data")

    return render(request, 'cloud/addmedia.html', {})


def addvideo1(request):
    return render(request, 'cloud/addmedia.html', {})


def av(request):
    vn = request.POST['videosname']
    vb = request.FILES['videosbrowse']

    extension = os.path.splitext(str(request.FILES['videosbrowse']))[1]
    ext = ['.mpg', '.mpeg', '.avi', '.wmv', '.mp4']
    if extension in ext:
        print("Data is saved")
        sv = addvideo(videosname=vn, videosbrowse=vb)
        sv.save()
    else:
        print("Enter correct data")
    return render(request, 'cloud/addmedia.html', {})


def register(request):
    return render(request, 'cloud/register.html', {})


def regs(request):
    un = request.POST['username']
    em = request.POST['email']
    pa = request.POST['password']
    ph = request.POST['phone']
    sv = usertable(username=un, email=em, password=pa, phone=ph)
    sv.save()
    return render(request, 'cloud/register.html', {})


def login(request):
    return render(request, 'cloud/login.html', {})


def checkuser(request):
    try:
        n1 = request.POST['username']
        n2 = request.POST['password']
        cus = usertable.objects.get(username=n1, password=n2)
        request.session['id'] = cus.id
        request.session['name'] = cus.username
        return home(request)
    except Exception as e:
        print(e)
        return render(request, 'cloud/login.html', {'error': 'invalid username or password'})


def logout(request):
    del request.session['id']
    del request.session['name']
    return home(request)

def search1(request):
    d = request.POST['search']
    p = addphoto.objects.get(photosname=d)
    return render(request, 'cloud/search.html', {'p': p})