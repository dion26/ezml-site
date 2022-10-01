from dataclasses import field
from rest_framework import serializers
from django_countries.serializer_fields import CountryField
from .models import Player, Position, SocialMedia

class PlayerSerializer(serializers.ModelSerializer):
    country = CountryField()
    class Meta:
        model = Player
        fields = [
            'public_id',
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
            'status',
            'dob',
        ]

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position

class SocialMediaSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='public_id', 
                        queryset=Player.objects.all())
    class Meta:
        model = SocialMedia
        fields = [
            'owner',
            'tiktok',
            'vk',
            'facebook',
            'instagram',
            'youtube',
        ]