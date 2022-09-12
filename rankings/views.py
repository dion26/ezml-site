from django.shortcuts import render
from django.http import HttpResponse

def rankings(request):
    return render(request, 'rankings/rankings.html')