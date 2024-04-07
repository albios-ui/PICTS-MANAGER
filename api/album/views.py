from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class AlbumView(View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=int(kwargs['uid']))
        output = ""
        for album in Album.objects.filter(user=user):
            output += str(album.user.id) + ":"+ str(album.album.id)+"\n"
        return HttpResponse(output)
class AlbumCreationView(View):
    def post(self, request, *args, **kwargs):
        userParam = request.POST['user']
        nameParam = request.POST['name']
        user = User.objects.get(pk=int(userParam))
        album = Album(name=nameParam, user=user)
        album.save()
        return HttpResponse("Successfully added album")
