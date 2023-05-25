from django.urls import path
# from cru_tes_kualifikasi.views import indexDataKualifikasi, indexPertanyaanKualifikasi
from cru_tes_kualifikasi.views import tes_kualifikasi, list_ujian_kualifikasi, riwayat_ujian_kualifikasi
from cru_tes_kualifikasi.views import form_buat_ujian_kualifikasi, list_ujian_kualifikasi_umpire, riwayat_ujian_kualifikasi_umpire

app_name = 'cru_tes_kualifikasi'

urlpatterns = [
    # path('data_kualifikasi/', indexDataKualifikasi, name='index'),
    # path('pertanyaan_kualifikasi/', indexPertanyaanKualifikasi, name='index'),
    path('tes-kualifikasi/', tes_kualifikasi, name='tes_kualifikasi' ),
    path('list-ujian-kualifikasi/', list_ujian_kualifikasi, name='list_ujian_kualifikasi' ),
    path('riwayat-ujian-kualifikasi/', riwayat_ujian_kualifikasi, name='riwayat_ujian_kualifikasi' ),

    path('form-buat-ujian-kualifikasi/', form_buat_ujian_kualifikasi, name='form_buat_ujian_kualifikasi' ),
    path('list-ujian-kualifikasi-umpire/', list_ujian_kualifikasi_umpire, name='list_ujian_kualifikasi_umpire' ),
    path('riwayat-ujian-kualifikasi-umpire/', riwayat_ujian_kualifikasi_umpire, name='riwayat_ujian_kualifikasi_umpire' ),
]