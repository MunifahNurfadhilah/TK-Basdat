from django.shortcuts import render
from Util.query import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.shortcuts import render

def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def indexDaftarSponsor(request):
    cursor = connection.cursor
    if request.method == 'POST':
        # Handle form submission
        nama_sponsor = request.POST.get('nama-sponsor')
        tanggal_mulai = request.POST.get('start-date')
        tanggal_selesai = request.POST.get('finish-date')
        
        # Do something with the data (e.g. save to database)
        # ...
        
        # Render a success message
        return render(request, 'daftar_sponsor.html')
    
    # Render the form template
    return render(request, 'daftar_sponsor.html')



def indexListSponsor(request):
     # events = Event.objects.all()
    cursor = connection.cursor
    query = f"""
        select nama_brand, tgl_mulai, tgl_selesai
        from sponsor as s, atlet_sponsor as asp, atlet as a
        where a.id='89c0bee8-0acc-4d61-8926-8c18482f3bdf' and s.id=asp.id_sponsor and a.id=asp.id_atlet;
    """

    cursor.execute('SET search_path TO babadu;')
    cursor.execute(query)

    
    data = fetch(cursor)

    response = {'data': data}
    print(response)
    
    return render(request, 'sponsor_cards.html', response)