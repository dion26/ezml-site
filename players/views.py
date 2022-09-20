from django.shortcuts import render
from players.models import Player
from django.views.generic.detail import DetailView

from rest_framework import generics
from .serializers import PlayerSerializer

class PlayerDetailView(DetailView):
    model = Player
    template_name= 'players/player.html'
    context_object_name = 'player'
    slug_field = "slug"
    query_pk_and_slug = True

class PlayerDetailAPIView(generics.RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    