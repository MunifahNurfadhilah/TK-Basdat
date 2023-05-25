from django.shortcuts import render
from django.shortcuts import render
from Util.query import *
from django.urls import reverse
from django.shortcuts import redirect, render
from django.db import connection
import random
from django.shortcuts import render, redirect


def fetch(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# Create your views here.

def indexEnrolledPartaiKompetisi(request):
    cursor = connection.cursor()
    cursor.execute('set search_path to babadu')
    email = request.COOKIES.get('email')
    nama = request.COOKIES.get('nama')

    cursor.execute(f"""
        SELECT id from MEMBER WHERE nama = {nama} and email = {email}; 
        """)

    record = cursor.fetchall()[0]
    id = record[0]

    cursor.execute(
        f"""
        SELECT pk.nama_event, pk.tahun_event, e.nama_stadium, ppk.jenis_partai, e.kategori_superseries, e.tgl_mulai, e.tgl_selesai
    FROM PARTAI_KOMPETISI pk
    JOIN PARTAI_PESERTA_KOMPETISI ppk ON pk.nama_event = ppk.nama_event AND pk.tahun_event = ppk.tahun_event AND pk.jenis_partai = ppk.jenis_partai
    JOIN EVENT e ON pk.nama_event = e.nama_event AND pk.tahun_event = e.tahun
    WHERE ppk.nomor_peserta = {id}"""
    )

    record = cursor.fetchall()[0]
    nama_event = record[0]
    tahun_event = record[1]
    nama_stadium = record[2]
    jenis_partai = record[3]
    kategori_superseries = record[4]
    tgl_mulai = record[5]
    tgl_selesai = record[6]

    context = {
        'nama_event': nama_event,
        'tahun_event': tahun_event,
        'nama_stadium': nama_stadium,
        'jenis_partai': jenis_partai,
        'kategori_superseries' : kategori_superseries,
        'tgl_mulai' : tgl_mulai,
        'tgl_selesai' : tgl_selesai

    }

    return render(request, 'enrolled_event_atlet.html', context)


def indexEnrolledEventAtlet(request):
    cursor = connection.cursor()
    cursor.execute('set search_path to babadu')

    email = request.COOKIES.get('email')
    nama = request.COOKIES.get('nama')

    cursor.execute(f"""
        SELECT id from MEMBER WHERE nama = {nama} and email = {email}; 
        """)

    
    record = cursor.fetchall()[0]
    id = record[0]

    cursor.execute('SET search_path TO babadu')
    cursor.execute(f"""
        SELECT e.nama_event, e.tahun, e.nama_stadium, e.kategori_superseries, e.tgl_mulai, e.tgl_selesai
            FROM babadu.event AS e, babadu.peserta_mendaftar_event AS pme, babadu.peserta_kompetisi AS pk
            WHERE pk.nomor_peserta = {id}
            AND pme.nomor_peserta = pk.nomor_peserta
            AND pme.nama_event = e.nama_event
            AND pme.tahun = e.tahun
    """)

    data = fetch(cursor)

    response = {'data': data}
    print(response)
    return render(request, 'event_cards_partai.html', response)


def deletePeserta(request):
    cursor = connection.cursor()
    cursor.execute('set search_path to babadu')


    no_peserta = request.COOKIES.get('no_peserta')
    nama_event = request.COOKIES.get('nama_event')
    tahun = request.COOKIES.get('tahun')

    cursor.execute('SET search_path TO babadu')

    cursor.execute(f"""
        DELETE FROM PESERTA_MENDAFTAR_EVENT WHERE no_peserta = {no_peserta} and nama_event = {nama_event} and tahun = {tahun}
        """)

    return indexEnrolledEventAtlet(request)





