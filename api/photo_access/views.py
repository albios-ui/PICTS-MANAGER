from django.shortcuts import render
from django.views.generic import View
from photo_access.models import PhotoAccess
from photo.models import Photo
from users.models import User
from django.http import HttpResponse

class PhotoAccessAddView(View):
    def post(self, request, *args, **kwargs):
        photoParam = request.POST['photo']
        userParam = request.POST['user']
        photo = Photo.objects.get(pk=int(photoParam))
        user = User.objects.get(pk=int(userParam))
        photo_access = PhotoAccess(photo=photo, user=user)
        photo_access.save()
        return HttpResponse("Successfully shared access")
class PhotoAccessView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=int(kwargs['uid']))
        output = ""
        for photo_access in PhotoAccess.objects.filter(user=user):
            output += str(photo_access.user.id) + ":"+ str(photo_access.photo.id)+"\n"
        return HttpResponse(output)
