def validasi_angka(teks):

    try:
        nilai = float(teks)
        return nilai

    except ValueError:
        return None