from django.shortcuts import render

# Create your views here.

def profile (request):
    context = {
        
    }
    return render(request, 'pages/profile.html', context)