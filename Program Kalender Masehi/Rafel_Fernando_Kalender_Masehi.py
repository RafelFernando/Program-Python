import calendar

# membuat inputan tahun dan bulan
tahun_kalender_masehi = int(input("Masukkan tahun: "))
bulan_kalender_masehi = int(input("Masukkan bulan: "))

# memanggil hasil inputan yang diterima
kalender_masehi = calendar.month(tahun_kalender_masehi, bulan_kalender_masehi)

# menampilkan kalender
print(kalender_masehi)