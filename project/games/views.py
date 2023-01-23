from django.shortcuts import render, get_object_or_404
from .models import *
from streams.models import *
# Create your views here.

def index(request):
    games = Game.objects.all()
    context = {
        'games': games,

    }
    return render(request, 'pages/index.html', context)


def details(request, id):
    game = get_object_or_404(Game, id = id)
    context = {
        'game' : game,
        'images' : game.images,

    }
    return render(request, 'pages/details.html', context)


def browse(request):
    streams = Stream.objects.all()
    games = Game.objects.all()
    context = {
        'streams' : streams,
        'games' : games,
        
    }
    return render(request, 'pages/browse.html', context)