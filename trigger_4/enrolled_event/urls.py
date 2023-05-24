from django.urls import path
from enrolled_event.views import indexEnrolledEventAtlet

app_name = 'enrolled_event'

urlpatterns = [
    path('enrolled_event_atlet/', indexEnrolledEventAtlet, name='index'),
]