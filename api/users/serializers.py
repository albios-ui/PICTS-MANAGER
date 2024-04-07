from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User
from rest_framework import serializers

class TokenAccessSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        return token

    def validate(self, attrs):
        data = super(TokenAccessSerializer, self).validate(attrs)
        data.update({'user_id': self.user.id})
        return data