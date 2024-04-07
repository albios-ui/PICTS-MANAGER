from django.db import models

from album.models import Album
from users.models import User

class AlbumAccess(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)