from django.urls import path
from cru_daftar_event.views import list_all_events, list_all_event_stadiums, list_all_event_categories

app_name = 'cru_daftar_event'

urlpatterns = [
    path('list_event/', list_all_events, name='index'),
    path('list_event_stadium/', list_all_event_stadiums, name='index'),
    path('list_event_kategori/', list_all_event_categories, name='index'),
]