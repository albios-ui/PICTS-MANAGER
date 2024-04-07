import base64
import io
import os

from PIL import Image
from django.core.files.base import ContentFile
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status, response

from .models import Photo
from .serializers import PhotoSerializer

from rest_framework.decorators import api_view


@api_view(["GET", "POST"])
def photo_list(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return JsonResponse({'photos': serializer.data})
    if request.method == 'POST':
        try:
            serializer = PhotoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)

@api_view(["GET", "POST"])
def save_file(request):
    if request.method == 'POST':
        file = request.data.get("file")
        name = request.data.get("name")
        try:
            ph = base64.b64decode(str(file))
            photo = Image.open(io.BytesIO(ph))
            path = os.getcwd() + "/" +request.data.get("album") +"/" + name
            photo.save(path, "jpeg")
        except Exception as e:
            print(e)


