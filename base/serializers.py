from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)

class CustomLoginSerializer(LoginSerializer):
    username = None