class showroom:
    def __init__(self, mobil, harga_mobil):
        self.mobil = str(mobil)
        self.harga = str(harga_mobil)
    def getJudul(self):
        return self.mobil
    def getNomor(self):
        return self.harga

Daftar_mobil = {}
loop = True
print("====================================")
print("Daftar Mobil Nasmoco")
print("====================================")
print(" MENU ")
print("1. Tambah Mobil =")
print("2. Hapus Mobil =")
print("3. Tampilkan Daftar Mobl =")
print("0. Exit/Keluar =")
print("=====================================")
print("\n\n")
while(loop):
    menu = input("Masukan Menu : ")
    if menu == "1":
        mobil = input("Masukan Mobil : ")
        harga = input("Masukan Harga : ")
        book = showroom(mobil, harga)
        Daftar_mobil[mobil] = book
    elif menu == "2":
        mobil = input("Masukan Nama Mobil : ")
        if(mobil in Daftar_mobil):
            del Daftar_mobil[mobil]
        else:
            print("Data Tidak Ditemukan")
    elif menu == "3":
        for x in Daftar_mobil:
            print("Nama Mobil Yang Tersedia : ", Daftar_mobil[x].getJudul())
            print("Harga Mobil : ", Daftar_mobil[x].getNomor())
    elif menu == "0":
        loop = False
    else:
        print("Perintah Tidak Ditemukan")        