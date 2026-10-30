def simpan_riwayat(teks):

    with open(
        "data/riwayat.txt",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(teks + "\n")