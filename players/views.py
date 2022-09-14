from django.shortcuts import render
from players.models import Player
from django.views.generic.detail import DetailView

class PlayerDetailView(DetailView):
    model = Player
