from src.converter import *
from src.validator import validasi_angka
from src.file_manager import simpan_riwayat

while True:

    print("\n===== KONVERSI SATUAN =====")
    print("1. Meter ke Centimeter")
    print("2. Centimeter ke Meter")
    print("3. Kilometer ke Meter")
    print("4. Meter ke Kilometer")
    print("5. Keluar")

    pilihan = input("Pilih menu : ")

    if pilihan == "5":
        print("Program selesai")
        break

    angka = input("Masukkan nilai : ")

    nilai = validasi_angka(angka)

    if nilai is None:
        print("Input harus angka")
        continue

    if pilihan == "1":

        hasil = meter_ke_cm(nilai)

        teks = f"{nilai} meter = {hasil} cm"

    elif pilihan == "2":

        hasil = cm_ke_meter(nilai)

        teks = f"{nilai} cm = {hasil} meter"

    elif pilihan == "3":

        hasil = km_ke_meter(nilai)

        teks = f"{nilai} km = {hasil} meter"

    elif pilihan == "4":

        hasil = meter_ke_km(nilai)

        teks = f"{nilai} meter = {hasil} km"

    else:

        print("Menu tidak tersedia")
        continue

    print(teks)

    simpan_riwayat(teks)