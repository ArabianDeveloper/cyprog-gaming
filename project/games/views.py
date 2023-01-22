from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        
    }
    return render(request, 'pages/index.html', context)


def details(request):
    context = {
        
    }
    return render(request, 'pages/details.html', context)


def browse(request):
    context = {
        
    }
    return render(request, 'pages/browse.html', context)