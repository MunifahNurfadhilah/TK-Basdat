from django.shortcuts import render

# Create your views here.

def indexListEvent(request):
    return render(request, 'list_event.html')

def indexListEventStadium(request):
    return render(request, 'list_event_stadium.html')

def indexListEventKategori(request):
    return render(request, 'list_event_kategori.html')