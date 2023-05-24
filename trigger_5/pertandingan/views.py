from django.shortcuts import render

# Create your views here.

def indexPerempat(request):
    return render(request, 'perempat.html')

def indexSemifinal(request):
    return render(request, 'semifinal.html')

def indexPerebutan3(request):
    return render(request, 'perebutan3.html')

def indexFinal(request):
    return render(request, 'final.html')

def indexPoin(request):
    return render(request, 'poin.html')