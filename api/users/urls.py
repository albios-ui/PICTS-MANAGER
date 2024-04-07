from django.urls import path

from . import views
from users.views import UserView
from users.views import UserGetView
from users.views import LoginView
from users.views import UserGetIdView

urlpatterns = [
    path("<int:id>", UserGetView.as_view()),
    path("<str:name>", UserGetIdView.as_view()),
    path("", UserView.as_view()),
    path("login", LoginView.as_view()),
]