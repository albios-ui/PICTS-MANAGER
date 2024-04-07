from django.urls import path

from . import views
from album_access.views import AlbumAccessView
from album_access.views import AlbumAccessCreationView

urlpatterns = [
    path('<int:uid>', AlbumAccessView.as_view()),
    path('', AlbumAccessCreationView.as_view()),
]