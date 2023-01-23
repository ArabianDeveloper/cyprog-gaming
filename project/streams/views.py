from django.shortcuts import render
from .models import *
from games.models import *
# Create your views here.

def streams(request):
    games = Game.objects.all()
    streams = Stream.objects.all()
    context = {
        'streams' : streams,
        'games' : games,

    }

    return render(request, 'pages/streams.html', context)