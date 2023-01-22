from django.shortcuts import render

# Create your views here.

def streams(request):
    context = {

    }

    return render(request, 'pages/streams.html', context)