def jenis_armada(jumlah_penumpang):
    if jumlah_penumpang >= 40 and jumlah_penumpang <=55:
        return "Big Bus"
    elif jumlah_penumpang >= 29 and jumlah_penumpang <=39:
        return "Medium Bus"
    else:
        return "Elf"

def tampilkan_menu_paket():
    print("Pilihan Paket")
    print("1. Paket A")
    print("   => Pantai Parangtritis")
    print("   => Malioboro")
    print("   => Candi Prambanan")
    print("2. Paket B")
    print("   => Bromo")
    print("   => Lautan Pasir")
    print("   => Savana")
    print("3. Paket C")
    print("   => Pantai Pandawa")
    print("   => Garuda Wisnu Kencana")
    print("   => Bedugul")

def tujuan_wisata(pilihan_paket):
    if pilihan_paket == "1":
        return "Pantai Parangtritis, Malioboro, Candi Prambanan"
    elif pilihan_paket == "2":
        return "Bromo, Lautan Pasir, Savana"
    elif pilihan_paket == "3":
        return "Pantai Pandawa, Garuda Wisnu Kencana, Bedugul"
    else:
        return "Tujuan wisata tidak valid"

def hitung_biaya_wisata(jumlah_penumpang, paket, armada):
    harga_sewa_bigbus = 5000000
    harga_sewa_mediumbus = 3500000
    harga_sewa_elf = 1500000
    harga_paket = 0

    if paket == "1":
        harga_paket = 100000
    elif paket == "2":
        harga_paket = 500000
    elif paket == "3":
        harga_paket = 1000000
    else:
        print("Paket Tidak Tersedia")
        return 0

    if armada == "Big Bus":
        total_biaya = harga_sewa_bigbus + (harga_paket * jumlah_penumpang)
    elif armada == "Medium Bus":
        total_biaya = harga_sewa_mediumbus + (harga_paket * jumlah_penumpang)
    elif armada == "Elf":
        total_biaya = harga_sewa_elf + (harga_paket * jumlah_penumpang)
    else:
        print("Jenis armada tidak valid")
        return 0

    return total_biaya

def nota(jumlah_penumpang, paket, armada, total_biaya, tujuan_wisata):
    print("-------------------------------------")
    print("----- Kwitansi Travel Mas Rafel -----")
    print("-------------------------------------")
    print("   Nama Customer    = ", customer)
    print("   Jumlah Penumpang = ", jumlah_penumpang)
    print("   Jenis Armada     = ", armada)
    print("   Paket            = ", paket)
    print("   Tujuan           = ", tujuan_wisata)
    print("   Biaya Total      = ", total_biaya)
    print("-------------------------------------")
    print("   Fasilitas = ")
    print("    => Armada Executive, Full Karaoke")
    print("    => Tour Leader")
    print("    => Tiket Masuk Semua Wisata")
    print("    => MMT Untuk Foto dan Bus")
    print("    => Makan Siang Prasmanan")
    print("    => Snack Pagi")
    print("    = P3K")
    print("-------------------------------------")

print("----------------------------------")
print("Selamat Datang Di Travel Mas Rafel")
print("----------------------------------")
customer = input("Masukkan Nama Anda: ")
jumlah_penumpang = int(input("Masukkan Jumlah Penumpang: "))
jenis = jenis_armada(jumlah_penumpang)
print("Armada yang digunakan adalah", jenis)
if jenis == "Big Bus" or jenis == "Medium Bus" or jenis == "Elf":
    tampilkan_menu_paket()
    pilihan_paket = input("Pilih Paket: ")
    tujuan = tujuan_wisata(pilihan_paket)
    total = hitung_biaya_wisata(jumlah_penumpang, pilihan_paket, jenis)
    nota(jumlah_penumpang, pilihan_paket, jenis, total, tujuan)
else:
    print("Tidak ada bus yang sesuai untuk jumlah penumpang", jumlah_penumpang)