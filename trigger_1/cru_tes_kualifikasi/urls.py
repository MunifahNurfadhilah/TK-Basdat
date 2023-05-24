from django.urls import path
from cru_tes_kualifikasi.views import indexDataKualifikasi, indexPertanyaanKualifikasi

app_name = 'cru_tes_kualifikasi'

urlpatterns = [
    path('data_kualifikasi/', indexDataKualifikasi, name='index'),
    path('pertanyaan_kualifikasi/', indexPertanyaanKualifikasi, name='index'),
]