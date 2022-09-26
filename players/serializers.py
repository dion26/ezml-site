from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    country = CountryField()
    class Meta:
        model = Player
        fields = [
            'nickname',
            'fullname',
            'role',
            'country',
            'slug',
            'image',
            'position',
            'get_age',
            'alternate_ids',
            'earning',
            'status'
        ]