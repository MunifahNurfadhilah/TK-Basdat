# atlet
def sql_get_list_ujian_kualifikasi():
    return f"""
    SELECT
        Tahun,
        Batch,
        Tempat,
        Tanggal
    FROM UJIAN_KUALIFIKASI
    """

def sql_get_riwayat_ujian_kualifikasi(id):
    return f"""
    SELECT tahun, batch, tempat, tanggal, hasil_lulus 
    FROM ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI a 
    JOIN MEMBER m ON a.ID_Atlet = m.id 
    WHERE id_atlet = '{id}';
    """

def sql_insert_riwayat_ujian_kualifikasi(id, tahun, batch, tempat, tanggal, hasil_lulus):
    return f"""
    INSERT INTO 
        ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI(ID_Atlet, tahun, batch, tempat, tanggal, hasil_lulus)
    VALUES
        (
            '{id}',
            '{tahun}',
            '{batch}',
            '{tempat}',
            '{tanggal}',
            '{hasil_lulus}'
        )
    """

# umpire
def sql_insert_ujian_kualifikasi(tahun, batch, tempat, tanggal):
    return f"""
    INSERT INTO 
        UJIAN_KUALIFIKASI(Tahun, Batch, Tempat, Tanggal)
    VALUES
        (
            '{tahun}',
            '{batch}',
            '{tempat}',
            '{tanggal}'
        )

    """

def sql_get_list_ujian_kualifikasi_umpire():
    return f"""
    SELECT
        Tahun,
        Batch,
        Tempat,
        Tanggal
    FROM UJIAN_KUALIFIKASI
    """

def sql_get_riwayat_ujian_kualifikasi_umpire():
    return f"""
    SELECT
        nama,
        tahun,
        batch,
        tempat,
        tanggal,
        Hasil_Lulus
    FROM ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI a JOIN MEMBER m ON a.ID_Atlet = m.id
    """