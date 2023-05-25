def sql_get_all_events():
    return """
    SELECT * 
    FROM EVENT;
    """

def sql_get_all_event_stadiums():
    return """
    SELECT e.nama_event, e.tahun, s.nama as nama_stadium, s.alamat as alamat_stadium
    FROM EVENT e
    JOIN STADIUM s ON e.nama_stadium = s.nama;
    """

def sql_get_all_event_categories():
    return """
    SELECT nama_event, tahun, kategori_superseries as kategori_event
    FROM EVENT;
    """