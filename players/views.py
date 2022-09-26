from django.shortcuts import render
from players.models import Player
from django.views.generic.detail import DetailView

from rest_framework import generics
from .serializers import PlayerSerializer
from .models import Player
from django.shortcuts import get_object_or_404

class PlayerDetailView(DetailView):
    model = Player
    template_name= 'players/player.html'
    context_object_name = 'player'
    slug_field = "slug"
    query_pk_and_slug = True

class PlayerDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        player_id = self.kwargs['pk']
        player_slug = self.kwargs['slug']
        return Player.objects.filter(id=player_id, slug=player_slug)
    
    