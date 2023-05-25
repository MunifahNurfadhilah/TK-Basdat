from django.db import connection, DatabaseError, IntegrityError
from collections import namedtuple
from django.shortcuts import redirect, render
from django.contrib import messages
import psycopg2
import locale
import uuid
locale.setlocale(locale.LC_ALL, '')


def map_cursor(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple("Result", [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def query(query_str: str):
    hasil = []
    with connection.cursor() as cursor:
        cursor.execute("SET SEARCH_PATH TO BABADU;")

        try:
            cursor.execute(query_str)

            if query_str.strip().lower().startswith("select"):
                # Kalau ga error, return hasil SELECT
                hasil = map_cursor(cursor)
            else:
                # Kalau ga error, return jumlah row yang termodifikasi oleh INSERT, UPDATE, DELETE
                hasil = cursor.rowcount
        except Exception as e:
            # Ga tau error apa
            hasil = e

    return hasil


# Create your views here.
db_connection = psycopg2.connect(
        host="containers-us-west-13.railway.app",
        database="railway",
        user="postgres",
        port="7337",
        password="a9nhUoVy1jPgQRnQs8qC"
    )
