from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from album_access.models import AlbumAccess
from album.models import Album
from users.models import User

class AlbumAccessView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=int(kwargs['uid']))
        output = ""
        for album_access in AlbumAccess.objects.filter(user=user):
            output += str(album_access.user.id) + ":"+ str(album_access.album.id)+"\n"
        return HttpResponse(output)
class AlbumAccessCreationView(View):
    def post(self, request, *args, **kwargs):
        albumParam = request.POST['album']
        userParam = request.POST['user']
        album = Album.objects.get(pk=int(albumAccess))
        user = User.objects.get(pk=int(userParam))
        album_access = AlbumAccess(album=album, user=user)
        album_access.save()
        return HttpResponse("Successfully shared access")