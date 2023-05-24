from django.urls import path
from daftar_sponsor.views import indexDaftarSponsor

app_name = 'daftar_sponsor'

urlpatterns = [
    path('daftar_sponsor/', indexDaftarSponsor, name='index'),
]