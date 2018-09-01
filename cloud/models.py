from django.db import models


class usertable(models.Model):
    username = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)


class addphoto(models.Model):
    photosname = models.CharField(max_length=100)
    photosbrowse = models.FileField()


class addaudio(models.Model):
    audiosname = models.CharField(max_length=100)
    audiosbrowse = models.FileField()


class addvideo(models.Model):
    videosname = models.CharField(max_length=100)
    videosbrowse = models.FileField()

