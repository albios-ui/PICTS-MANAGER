from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    is_favorite = models.BooleanField()
    is_default = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    snap_date = models.DateTimeField()
    snap_place = models.CharField(max_length=1000)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


class PhotoAccess(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class AlbumAcces(models.Model):
    id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Preferences(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
