from django.shortcuts import render

# Create your views here.

def indexCR(request):
    return render(request, 'cr_daftar_atlet.html')

def indexListAtlet(request):
    return render(request, 'list_atlet.html')