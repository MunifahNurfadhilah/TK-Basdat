from django.urls import path
from event_umpire.views import indexEventUmpire

app_name = 'event_umpire'

urlpatterns = [
    path('event_umpire/', indexEventUmpire, name='index'),
]