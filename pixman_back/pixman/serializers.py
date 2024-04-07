from rest_framework import serializers

from pixman.models import Photo
from pixman.models import Album


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'user', 'name', 'snap_date',  'snap_place', 'album']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'is_favorite', 'is_default', 'user']



