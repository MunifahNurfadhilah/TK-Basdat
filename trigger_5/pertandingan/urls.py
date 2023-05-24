from django.urls import path
from pertandingan.views import indexPerempat, indexSemifinal, indexPerebutan3, indexFinal, indexPoin


app_name = 'pertandingan'

urlpatterns = [
    path('perempat/', indexPerempat, name='index'),
    path('semifinal/', indexSemifinal, name='index'), 
    path('perebutan3/', indexPerebutan3, name='index'), 
    path('final/', indexFinal, name='index'), 
    path('poin/', indexPoin, name='index'), 
]