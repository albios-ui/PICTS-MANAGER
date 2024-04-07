from django.shortcuts import render
from django.views.generic import View
from photo.models import Photo
from album.models import Album
from users.models import User
from django.http import HttpResponse
import os

path = "photos/"

class PhotoAddView(View):
    def post(self, request, *args, **kwargs):
        ownerParam = request.POST.get('owner', False)
        dataParam = request.POST.get('data', False)
        owner = User.objects.get(pk=int(ownerParam))
        
        if request.POST.get('album', False):
            album = Album.objects.get(pk=int(request.POST.get('album', False)))
            photo = Photo(album=album, owner=owner)
        else:
            photo = Photo(owner=owner)
        photo.save()
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(path+str(owner.id)):
            os.mkdir(path+str(owner.id))
        f = open(path+str(owner.id)+"/"+str(photo.id), "w")
        f.write(dataParam)
        f.close()
        return HttpResponse("Successfully shared access")
class PhotoView(View):
    def get(self, request, *args, **kwargs):
        ownerParam = kwargs['uid']
        photoParam = kwargs['photo_id']
        file = open(path+str(ownerParam)+"/"+str(photoParam), "r+")
        return HttpResponse(file.read())