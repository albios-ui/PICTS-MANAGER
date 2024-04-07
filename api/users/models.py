from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)

class UserManager(BaseUserManager):
    use_in_migrations = True
    
    def _create_user(self, username, password):
        if not username:
            raise ValueError("Username not set")
        username = self.normalize_email(username)
        user = self.model(username=username)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, password=None, **args):
        return self._create_user(username, password)

class User(AbstractBaseUser):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    USERNAME_FIELD = "username"
    objects = UserManager()