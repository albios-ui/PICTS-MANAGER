from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
import os
from .models import Photo, Album
from .serializers import PhotoSerializer, AlbumSerializer

from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def album_list(request):
    if request.method == 'GET':
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return JsonResponse({'albums': serializer.data})
    if request.method == 'POST':
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            print(request.data["name"])
            album_path = os.getcwd() + "/" + request.data["name"]
            if not os.path.exists(album_path):
                os.makedirs(album_path, 0o777)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def get_album(request, name):
    try:
        album = Album.objects.get(name=name)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AlbumSerializer(album)
    return Response(serializer.data)
    # default_album = Album.objects.raw("SELECT all FROM pixman_album pa WHERE pa.user_id = " + request.data['user'] + " AND pa.is_default = true")
