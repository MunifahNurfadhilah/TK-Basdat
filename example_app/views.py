from django.shortcuts import render
from Util.query import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
import uuid

def index(request):
    return render(request, 'index.html')

def indexWelcome(request):
    return render(request, 'welcome.html')

def indexLogin(request):
    if request.method == 'POST' or 'post' and not request.method == 'GET':
        name = request.POST.get('name')
        email = request.POST.get('email')
        id = uuid.uuid4()

        cursor.execute(f"""
        INSERT INTO MEMBER VALUES ({id}, {email}, {name});
        """)


    return render(request, 'loginForm.html')