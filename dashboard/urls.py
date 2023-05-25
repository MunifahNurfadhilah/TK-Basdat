from django.urls import path
from dashboard.views import indexDashboardAtlet, indexDashboardPelatih, indexDashboardUmpire

app_name = 'dashboard'

urlpatterns = [
    path('dashboard_atlet/', indexDashboardAtlet, name='dashboard_atlet'),
    path('dashboard_pelatih/', indexDashboardPelatih, name='dashboard_pelatih'),
    path('dashboard_umpire/', indexDashboardUmpire, name='dashboard_umpire'),    
]