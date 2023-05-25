from django.shortcuts import render, get_object_or_404
from .models import *
from streams.models import *
from accounts.models import *
# Create your views here.

def index(request):
    games = Game.objects.all()
    context = {
        'games': games,

    }
    return render(request, 'pages/index.html', context)


def details(request, slug):
    game = get_object_or_404(Game, slug = slug)
    games = Game.objects.all()
    context = {
        'game' : game,
        'games' : games,

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


def search(request):
    name = None
    if 'searchKeyword' in request.GET:
        name = request.GET['searchKeyword']
        if name:
            games = Game.objects.filter(name__icontains = name)
            users = User.objects.filter(username__icontains = name)
            streams = Stream.objects.filter(title__icontains = name)
        else:
            games = Game.objects.all()
            users = User.objects.all()
            streams = Stream.objects.all()

    context = {
        'games' : games,
        'users' : users,
        'streams' : streams, 
    }
    return render(request, 'pages/search.html', context)