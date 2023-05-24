from django.urls import path
from cru_daftar_event.views import indexListEvent, indexListEventStadium, indexListEventKategori

app_name = 'cru_daftar_event'

urlpatterns = [
    path('list_event/', indexListEvent, name='index'),
    path('list_event_stadium/', indexListEventStadium, name='index'),
    path('list_event_kategori/', indexListEventKategori, name='index'),
]