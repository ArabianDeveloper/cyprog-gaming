from django.shortcuts import render, get_object_or_404, redirect
from .models import *

# Create your views here.

def profile (request, slug):

    pro = get_object_or_404(Profile, slug = slug)

    context = {
        'profile': pro,
    }
    return render(request, 'pages/profile.html', context)

def UserProfile (request):

    pro = get_object_or_404(Profile, slug=request.user.profile.slug)

    context = {
        'profile': pro,
    }
    return render(request, 'pages/profile.html', context)


def addfriend(request, slug):
    print("done")
    friend = get_object_or_404(Profile, slug = slug)
    print(friend.user)
    if friend in request.user.friends.all:
        request.user.friends.remove(friend.user)
    else :
        request.user.friends.add(friend.user)
    print("done")
    return redirect('/')