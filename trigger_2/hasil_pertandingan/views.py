from django.shortcuts import render

# Create your views here.

def indexHasilPertandingan(request):
    return render(request, 'hasil_pertandingan.html')