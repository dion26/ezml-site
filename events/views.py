from django.shortcuts import render
from django.http import HttpResponse

def events(request):
    return render(request, 'events/events.html')