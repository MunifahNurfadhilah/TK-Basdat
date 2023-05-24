from django.shortcuts import render

# Create your views here.

def indexEventUmpire(request):
    return render(request, 'event_umpire.html')