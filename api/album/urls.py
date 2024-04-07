from django.urls import path

from . import views
from album.views import AlbumView
from album.views import AlbumCreationView

urlpatterns = [
    path(r'^(?P<id>[0-9]*)/$', AlbumView.as_view()),
    path(r'^/$', AlbumCreationView.as_view()),
]