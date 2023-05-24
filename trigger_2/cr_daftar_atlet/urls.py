from django.urls import path
from cr_daftar_atlet.views import indexCR, indexListAtlet

app_name = 'cr_daftar_atlet'

urlpatterns = [
    path('cr_daftar_atlet/', indexCR, name='index'),
    path('list_atlet/', indexListAtlet, name='index'),
]