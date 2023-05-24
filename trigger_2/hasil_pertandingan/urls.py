from django.urls import path
from hasil_pertandingan.views import indexHasilPertandingan


app_name = 'hasil_pertandingan'

urlpatterns = [
    path('hasil_pertandingan/', indexHasilPertandingan, name='index'),
]