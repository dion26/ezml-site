from dataclasses import fields
from rest_framework import serializers
from .models import Team, Membership
from players.models import Player

class TeamLookUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = [
            'public_id'
        ]

class MembershipSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(slug_field='public_id', queryset=Player.objects.all())
    team = serializers.SlugRelatedField(slug_field='public_id', queryset=Team.objects.all())
    class Meta:
        model = Membership
        fields = [
            "player",
            "team",
            "date_joined",
            "date_left",
            "status",
        ]

class TeamSerializer(serializers.ModelSerializer):
    members = serializers.SlugRelatedField(many=True, 
                                            read_only=True, 
                                            slug_field='public_id')
    class Meta:
        model = Team
        fields = [
            'public_id',
            'name',
            'logo',
            'slug',
            'members',
        ]
        depth = 1

