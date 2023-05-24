from django.shortcuts import render

# Create your views here.

def indexEnrolledEventAtlet(request):
    return render(request, 'enrolled_event_atlet.html')
