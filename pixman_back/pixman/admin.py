from django.contrib import admin
from .models import Photo
from .models import PhotoAccess
from .models import Album
from .models import AlbumAcces

admin.site.register(Photo)
admin.site.register(PhotoAccess)
admin.site.register(Album)
admin.site.register(AlbumAcces)