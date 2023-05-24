from django.shortcuts import render

# Create your views here.

def indexDataKualifikasi(request):
    return render(request, 'data_kualifikasi.html')

def indexPertanyaanKualifikasi(request):
    return render(request, 'pertanyaan_kualifikasi.html')
