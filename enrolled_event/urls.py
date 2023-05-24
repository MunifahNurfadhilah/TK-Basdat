from django.urls import path
from enrolled_event.views import indexEnrolledEventAtlet
from enrolled_event.views import indexEnrolledPartaiKompetisi

app_name = 'enrolled_event'

urlpatterns = [
    path('enrolled_event_atlet/', indexEnrolledEventAtlet, name='index'),
    path('enrolled_partai_kompetisi/', indexEnrolledPartaiKompetisi, name='index'),
    
]