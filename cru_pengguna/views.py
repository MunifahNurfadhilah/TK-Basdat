from django.shortcuts import render
from Util.query import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import random

def indexEarly(request):
    return render(request, 'early_register.html')

def indexRegistAtlet(request):
    cursor.execute('set search_path to babadu')
    if request.method == 'POST' or 'post' and not request.method == 'GET':

        name = request.POST.get('name')
        email = request.POST.get('email')

        cursor.execute(f"""
        SELECT id from MEMBER WHERE nama = {name} and email = {email}; 
        """)

        record = cursor.fetchall()[0]

        id = record[0]
        country = request.POST.get('country')
        dob = request.POST.get('dob')
        play = request.POST.get('play')
        height = request.POST.get('height')
        gender = request.POST.get('gender')

        cursor.execute(f"""
        INSERT INTO ATLET VALUES ({id}, {name}, {country}, {dob}, {play}, {height}, {gender});
        """)

    return render(request, 'regist_atlet.html')

def indexRegistPelatih(request):
    cursor.execute('set search_path to babadu')

    if request.method == 'POST' or 'post' and not request.method == 'GET':
        name = request.POST.get('name')
        email = request.POST.get('email')

        cursor.execute(f"""
        SELECT id from MEMBER WHERE nama = {name} and email = {email}; 
        """)

        record = cursor.fetchall()[0]

        id = record[0]
        country = request.POST.get('country')
        category = request.POST.getlist('category[]')
        dob = request.POST.get('dob')
        

        cursor.execute(f"""
        INSERT INTO UMPIRE VALUES ({id}, {name}, {country}, {category},{dob});
        """)
    return render(request, 'regist_pelatih.html')

def indexRegistUmpire(request): 
    cursor.execute('set search_path to babadu')
    if request.method == 'POST' or 'post' and not request.method == 'GET':
        name = request.POST.get('name')
        email = request.POST.get('email')

        cursor.execute(f"""
        SELECT id from MEMBER WHERE nama = {name} and email = {email}; 
        """)

        record = cursor.fetchall()[0]

        id = record[0]
        country = request.POST.get('country')

        cursor.execute(f"""
        INSERT INTO UMPIRE VALUES ({id}, {name}, {country});
        """)

    return render(request, 'regist_umpire.html')