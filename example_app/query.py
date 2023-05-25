def sql_insert_member(id, nama, email):
    return f"""
        INSERT INTO
            MEMBER (id, nama, email) 
        VALUES
            (
                '{id}',
                '{nama}',
                '{email}'
            );
        """

def sql_insert_umpire(id, negara):
    return f"""
        INSERT INTO
            UMPIRE (ID, Negara)
        VALUES
            (
                '{id}',
                '{negara}'
            );
        """

def sql_insert_pelatih(id, tanggal_mulai):
    return f"""
        INSERT INTO
            PELATIH (ID, Tanggal_Mulai)
        VALUES
            (
                '{id}',
                '{tanggal_mulai}'
            );
        """

def sql_insert_atlet(id, tgl_lahir, negara_asal, play_right, height, jenis_kelamin):
    return f"""
        INSERT INTO
            ATLET (
                ID,
                Tgl_Lahir,
                Negara_Asal,
                Play_Right,
                Height,
                World_Rank,
                Jenis_Kelamin
            )
        VALUES
            (
                '{id}',
                '{tgl_lahir}',
                '{negara_asal}',
                {play_right},
                {height},
                0,
                {jenis_kelamin}
            );
        """

def sql_insert_pelatih_spesialisasi(id_pelatih, spesialisasi):
    return f"""
        INSERT INTO 
            PELATIH_SPESIALISASI (ID_Pelatih, ID_Spesialisasi)
        SELECT 
            '{id_pelatih}', 
            ID FROM SPESIALISASI 
        WHERE Spesialisasi = '{spesialisasi}';
    """


def sql_get_user(nama, email):
    return f"""
        SELECT
            M.ID,
            M.Nama,
            M.Email,
            COALESCE(U.ID, P.ID, A.ID) AS ID_Member,
            CASE
                WHEN U.ID IS NOT NULL THEN 'umpire'
                WHEN P.ID IS NOT NULL THEN 'pelatih'
                WHEN A.ID IS NOT NULL THEN 'atlet'
                ELSE 'unknown'
            END AS tipe_member,
            U.Negara,
            P.Tanggal_Mulai,
            A.Tgl_Lahir,
            A.Negara_Asal,
            A.Play_Right,
            A.Height,
            A.World_Rank,
            A.Jenis_Kelamin
        FROM
            MEMBER AS M
            LEFT JOIN UMPIRE AS U ON M.ID = U.ID
            LEFT JOIN PELATIH AS P ON M.ID = P.ID
            LEFT JOIN ATLET AS A ON M.ID = A.ID
        WHERE
            M.Nama = '{nama}' and M.email = '{email}';
    """
