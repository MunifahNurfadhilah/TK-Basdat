# Create your views here.

# def indexDataKualifikasi(request):
#     return render(request, 'data_kualifikasi.html')

# def indexPertanyaanKualifikasi(request):
#     return render(request, 'pertanyaan_kualifikasi.html')


# Create your views here.

from django.shortcuts import render
# from project_django.helper.function import *
from django.shortcuts import render, redirect
from django.db import connection, InternalError
from cru_tes_kualifikasi.query import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import locale
import uuid
from utils.query import *
locale.setlocale(locale.LC_ALL, '')


# Create your views here.
def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# atlet
def tes_kualifikasi(request):
    return render(request, "tes-kualifikasi.html")

def list_ujian_kualifikasi(request):
    context = {}
    db_connection = psycopg2.connect(
        host="containers-us-west-13.railway.app",
        database="railway",
        user="postgres",
        port="7337",
        password="a9nhUoVy1jPgQRnQs8qC"
    )
    cursor = db_connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")

    #GET LIST UJIAN KUALIFIKASI
    query = sql_get_list_ujian_kualifikasi()
    cursor.execute(query)
    data = parse(cursor)
    list_ujian_kualifikasi = []
    for ujian_kualifikasi in data:
        # ujian_kualifikasi['slug'] = title_to_slug(ujian_kualifikasi['nama'])
        list_ujian_kualifikasi.append(ujian_kualifikasi)

    context['data_list_ujian_kualifikasi'] = list_ujian_kualifikasi

    return render(request, "list-ujian-kualifikasi.html", context)

def riwayat_ujian_kualifikasi(request):
    context = {}
    db_connection = psycopg2.connect(
        host="containers-us-west-13.railway.app",
        database="railway",
        user="postgres",
        port="7337",
        password="a9nhUoVy1jPgQRnQs8qC"
    )
    cursor = db_connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")

    #GET RIWAYAT UJIAN KUALIFIKASI
    query = sql_get_riwayat_ujian_kualifikasi(request.session['id'])
    cursor.execute(query)
    data = parse(cursor)
    riwayat_ujian_kualifikasi = []
    for r_ujian_kualifikasi in data:
        # ujian_kualifikasi['slug'] = title_to_slug(ujian_kualifikasi['nama'])
        riwayat_ujian_kualifikasi.append(r_ujian_kualifikasi)

    context['data_riwayat_ujian_kualifikasi'] = riwayat_ujian_kualifikasi

    return render(request, "riwayat-ujian-kualifikasi.html", context)

# umpire
def buat_tes_kualifikasi(tahun, batch, tempat, tanggal):
    try:
        db_connection = psycopg2.connect(
        host="containers-us-west-13.railway.app",
        database="railway",
        user="postgres",
        port="7337",
        password="a9nhUoVy1jPgQRnQs8qC"
        )
        cursor = db_connection.cursor()
        cursor.execute("SET SEARCH_PATH TO BABADU;")
        query = sql_insert_ujian_kualifikasi(tahun, batch, tempat, tanggal)
        cursor.execute(query)
    except InternalError as e:
        return {
            'success': False,
            'msg': str(e.args)
        }
    else:
        return {
            'success': True,
        }
    
@csrf_exempt
def form_buat_ujian_kualifikasi(request):
    if request.method == 'POST':
         if 'submitFormUjian' in request.POST:
            tahun = request.POST.get('tahun')
            batch = request.POST.get('batch')
            tempat = request.POST.get('tempat')
            tanggal = request.POST.get('tanggal')
            data = buat_tes_kualifikasi(tahun, batch, tempat, tanggal)
            if data['success']:
                return redirect('cru_tes_kualifikasi:list_ujian_kualifikasi_umpire')
            else:
                messages.info(request,data['msg'])
    return render(request, "form_buat_ujian_kualifikasi.html")

def list_ujian_kualifikasi_umpire(request):
    context = {}
    db_connection = psycopg2.connect(
        host="containers-us-west-13.railway.app",
        database="railway",
        user="postgres",
        port="7337",
        password="a9nhUoVy1jPgQRnQs8qC"
    )
    cursor = db_connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")

    #GET LIST UJIAN KUALIFIKASI
    query = sql_get_list_ujian_kualifikasi_umpire()
    cursor.execute(query)
    data = parse(cursor)
    list_ujian_kualifikasi_umpire = []
    for ujian_kualifikasi_umpire in data:
        # ujian_kualifikasi['slug'] = title_to_slug(ujian_kualifikasi['nama'])
        list_ujian_kualifikasi_umpire.append(ujian_kualifikasi_umpire)

    context['data_list_ujian_kualifikasi_umpire'] = list_ujian_kualifikasi_umpire
    return render(request, "list_ujian_kualifikasi_umpire.html", context)

def riwayat_ujian_kualifikasi_umpire(request):
    context = {}
    db_connection = psycopg2.connect(
        host="containers-us-west-13.railway.app",
        database="railway",
        user="postgres",
        port="7337",
        password="a9nhUoVy1jPgQRnQs8qC"
    )
    cursor = db_connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")

    #GET RIWAYAT UJIAN KUALIFIKASI
    query = sql_get_riwayat_ujian_kualifikasi_umpire()
    cursor.execute(query)
    data = parse(cursor)
    riwayat_ujian_kualifikasi_umpire = []
    for r_ujian_kualifikasi_umpire in data:
        # ujian_kualifikasi['slug'] = title_to_slug(ujian_kualifikasi['nama'])
        riwayat_ujian_kualifikasi_umpire.append(r_ujian_kualifikasi_umpire)

    context['data_riwayat_ujian_kualifikasi_umpire'] = riwayat_ujian_kualifikasi_umpire

    return render(request, "riwayat_ujian_kualifikasi_umpire.html", context)

