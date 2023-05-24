from django.shortcuts import render

# Create your views here.

def indexDaftarSponsor(request):
    return render(request, 'daftar_sponsor.html')