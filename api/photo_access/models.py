from django.db import models

from photo.models import Photo
from users.models import User

class PhotoAccess(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)