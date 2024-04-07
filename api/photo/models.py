from django.db import models

from album.models import Album
from users.models import User

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)