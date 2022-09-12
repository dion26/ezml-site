from django.shortcuts import render
from django.http import HttpResponse

list_match = [
    {'id':1, 'time': '26/08/2022/23/30', 'team1': 'RRQ', 'team2': 'EVOS', 'score': [1,2], 'status': 'Live', 'Event': 'MPL ID 2022'},
    {'id':2, 'time': '26/08/2022/23/30', 'team1': 'RRQ', 'team2': 'EVOS', 'score': [1,2], 'status': 'Live', 'Event': 'MPL ID 2022'},
    {'id':3, 'time': '26/08/2022/23/30', 'team1': 'RRQ', 'team2': 'EVOS', 'score': [1,2], 'status': 'Live', 'Event': 'MPL ID 2022'},
    ]

def matches(request):
    context = {'list_match': list_match}
    return render(request, 'matches/matches.html', context)