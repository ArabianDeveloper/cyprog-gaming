from django.shortcuts import render
from .models import *
from games.models import *
from accounts.models import *
from django.contrib.auth.models import User
# Create your views here.

def streams(request):
    games = Game.objects.all()
    streams = Stream.objects.all()
    users = User.objects.all()
    context = {
        'streams' : streams,
        'games' : games,
        'streamers' : users
    }

    return render(request, 'pages/streams.html', context)