from urllib import request
from django.shortcuts import render
from rest_framework import generics
from players.models import Player
from players.serializers import PlayerSerializer

class SearchListView(generics.ListAPIView):
    queryset = Player.search_objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = Player.objects.none()
        if q is not None and q is not '':
            results = qs.search(q)
        return results