from django.shortcuts import render

# Create your views here.

def list_all_events(request):
    context = {}
    db_connection = psycopg2.connect(
        host="localhost",
        database="munifah.nurfadhilah",
        user="postgres",
        port="5433",
        password="99tugas"
    )
    cursor = db_connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")
    query = sql_get_all_events()
    cursor.execute(query)
    data = cursor.fetchall()
    list_events = []
    for event in data:
        list_events.append(event)
    context['data_list_events'] = list_events
    return render(request, "list_events.html", context)

def list_all_event_stadiums(request):
    context = {}
    db_connection = psycopg2.connect(
        host="localhost",
        database="munifah.nurfadhilah",
        user="postgres",
        port="5433",
        password="99tugas"
    )
    cursor = db_connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")
    query = sql_get_all_event_stadiums()
    cursor.execute(query)
    data = cursor.fetchall()
    list_event_stadiums = []
    for event_stadium in data:
        list_event_stadiums.append(event_stadium)
    context['data_list_event_stadiums'] = list_event_stadiums
    return render(request, "list_event_stadiums.html", context)


def list_all_event_categories(request):
    context = {}
    db_connection = psycopg2.connect(
        host="localhost",
        database="munifah.nurfadhilah",
        user="postgres",
        port="5433",
        password="99tugas"
    )
    cursor = db_connection.cursor()
    cursor.execute("SET SEARCH_PATH TO BABADU;")
    query = sql_get_all_event_categories()
    cursor.execute(query)
    data = cursor.fetchall()
    list_event_categories = []
    for event_category in data:
        list_event_categories.append(event_category)
    context['data_list_event_categories'] = list_event_categories
    return render(request, "list_event_categories.html", context)
