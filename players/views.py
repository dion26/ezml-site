from django.shortcuts import render
from players.models import Player, SocialMedia

from rest_framework import generics, permissions
from .serializers import PlayerSerializer, SocialMediaSerializer
from .models import Player
from django.shortcuts import get_object_or_404
from api.mixins import MultipleFieldLookupMixin

class PlayerListApiView(generics.ListAPIView):
    serializer_class = PlayerSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Player.objects.all()

class PlayerDetailAPIView(MultipleFieldLookupMixin, 
                            generics.RetrieveAPIView):
    serializer_class = PlayerSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Player.objects.all()
    lookup_fields = ['public_id', 'slug']

class PlayerCreateAPIView(generics.CreateAPIView):
    serializer_class = PlayerSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Player.objects.all()

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(PlayerCreateAPIView, self).get_serializer(*args, **kwargs)

class PlayerUpdateAPIView(MultipleFieldLookupMixin,
                            generics.UpdateAPIView):
    serializer_class = PlayerSerializer
    lookup_fields = ['public_id', 'slug']
    permission_classes = [permissions.AllowAny]
    queryset = Player.objects.all()

class PlayerDeleteAPIView(generics.DestroyAPIView):
    serializer_class = PlayerSerializer

    def get_queryset(self):
        player_id = self.kwargs['public_id']
        player_slug = self.kwargs['slug']
        return Player.objects.filter(public_id=player_id, slug=player_slug)
    
class SocialCreateAPIView(generics.CreateAPIView):
    serializer_class = SocialMediaSerializer
    permission_classes = [permissions.AllowAny]
    queryset = SocialMedia.objects.all()

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(SocialCreateAPIView, self).get_serializer(*args, **kwargs)


class SocialDetailAPIView(generics.RetrieveAPIView):
    serializer_class = SocialMediaSerializer
    permission_classes = [permissions.AllowAny]
    queryset = SocialMedia.objects.all()
    
class SocialListApiView(generics.ListAPIView):
    serializer_class = SocialMediaSerializer
    permission_classes = [permissions.AllowAny]
    queryset = SocialMedia.objects.all()