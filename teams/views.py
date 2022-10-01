from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import TeamSerializer, MembershipSerializer
from .models import Membership, Team


class TeamListApiView(generics.ListAPIView):
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Team.objects.all()

class TeamCreateAPIView(generics.CreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Team.objects.all()

    def get_serializer(self, *args, **kwargs):

        if isinstance(kwargs.get("data", {}), list):
            kwargs['many'] = True

        return super(TeamCreateAPIView, self).get_serializer(*args, **kwargs)

class MembershipListApiView(generics.ListAPIView):
    serializer_class = MembershipSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Membership.objects.all()

class MembershipCreateApiView(generics.CreateAPIView):
    serializer_class = MembershipSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Membership.objects.all()

    def get_serializer(self, *args, **kwargs):

        if isinstance(kwargs.get("data", {}), list):
            kwargs['many'] = True

        return super(MembershipCreateApiView, self).get_serializer(*args, **kwargs)