from django.urls import path

from . import views
from photo_access.views import PhotoAccessView
from photo_access.views import PhotoAccessAddView

urlpatterns = [
    path("<int:uid>", PhotoAccessView.as_view()),
    path("", PhotoAccessAddView.as_view()),
]