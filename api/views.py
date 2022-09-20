
from django.http import JsonResponse
from django.forms.models import model_to_dict
import json
from players.models import Player
from forums.models import Thread

from rest_framework.response import Response
from rest_framework.decorators import api_view
from players.serializers import PlayerSerializer
from forums.serializers import ThreadSerializer
# Create your views here.

@api_view(["POST"])
def api_home(request, *args, **kwargs):
 
    data = request.data
    serializer = ThreadSerializer(data=data)
    print("inside api home")
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({"invalid": "invalid data given"}, status=400)