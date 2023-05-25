from django.urls import path
from example_app.views import index, indexWelcome, show_login, logout, show_register


app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', indexWelcome, name='welcome'),
    path('register/', show_register, name='register' ),
    path('loginForm/', show_login, name='loginForm'), 
    path('logout/', logout, name='logout'), 
]