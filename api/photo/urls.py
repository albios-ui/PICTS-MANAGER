from django.urls import path

from . import views
from photo.views import PhotoView
from photo.views import PhotoAddView

urlpatterns = [
    path("<int:uid>/<int:photo_id>", PhotoView.as_view()),
    path("", PhotoAddView.as_view()),
]