from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserView(View):
    def post(self, request, *args, **kwargs):
        try:
            User.objects.get(username=request.POST['username'])
            return HttpResponse("Already exist")
        except:
            user = User.objects.create_user(request.POST['username'], "")
            user.save()
            return HttpResponse(str(user.id))
    def delete(self, request, *args, **kwargs):
        return HttpResponse("DELETE request")
    def put(self, request, *args, **kwargs):
        return HttpResponse("PUT request")
class UserGetView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(str(User.objects.get(pk=kwargs['id'])))
class UserGetIdView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(str(User.objects.get(username=kwargs['name']).id))
class LoginView(View):
    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
            return HttpResponse("Login"+str(get_tokens_for_user(user)))
        except:
            return HttpResponse("Couldn't login")
            
