from django.shortcuts import render
from django.shortcuts import render
from Util.query import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
import random
from django.shortcuts import render, redirect


# Create your views here.

def indexEnrolledEventAtlet(request):
    cursor.execute('set search_path to babadu')
    email = request.COOKIES.get('email')

    cursor.execute(
        f"""
        SELECT pk.nama_event, pk.tahun_event, e.nama_stadium, ppk.jenis_partai, e.kategori_superseries, e.tgl_mulai, e.tgl_selesai
    FROM PARTAI_KOMPETISI pk
    JOIN PARTAI_PESERTA_KOMPETISI ppk ON pk.nama_event = ppk.nama_event AND pk.tahun_event = ppk.tahun_event AND pk.jenis_partai = ppk.jenis_partai
    JOIN EVENT e ON pk.nama_event = e.nama_event AND pk.tahun_event = e.tahun
    WHERE ppk.nomor_peserta = {email};"""
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
        'kategori_superseries' : kategori_superseries ,
        'tgl_mulai' : tgl_mulai,
        'tgl_selesai' : tgl_selesai

    }

    return render(request, 'enrolled_event_atlet.html', context)


def indexEnrolledPartaiKompetisi(request):

    return render(request, 'enrolled_partai_kompetisi.html')



