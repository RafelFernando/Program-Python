print("---------------------------------------------")
print("Selamat Datang Di Persewaan Mobil Pak Ferguso")
print("---------------------------------------------")
print()
nama = input("masukkan nama anda: ")
Mobil = ['avanza', 'innova','jazz','civic']
print("Pilihan Mobil")
print("a. toyota")
print("b. honda")
print()
jenis = input("pilih jenis (toyota/honda): ")
print(nama, "memilih mobil", jenis)
if jenis == 'toyota' :
    print("1." ,Mobil[0] ) 
    print("2.",Mobil[1] )
elif  jenis == 'honda':    
    print("1." ,Mobil[2] )
    print("2.",Mobil[3] )
else :
    print("Mobil Tidak Tersedia")
merk_mobil = input("Pilih merk mobil: ")
if merk_mobil == 'avanza':
    print("Harga sewa = Rp 350.000/hari")
    harga=350000
    lama_pinjam = int(input("Masukkan lama pinjaman(dalam hitungan hari): "))
    total =harga*lama_pinjam
    print("Total harga yang harus dibayar : Rp. ",total)
elif merk_mobil == 'innova':
    print("Harga sewa = Rp 425.000/hari") 
    harga=425000
    lama_pinjam = int(input("Masukkan lama pinjaman(dalam hitungan hari): "))
    total1 =harga*lama_pinjam
    asuransi =total1*0.1
    total =total1+asuransi
    print("Total harga yang harus dibayar : Rp. ",total)
elif merk_mobil == 'jazz':
    print("Harga sewa = Rp 375.000/hari")
    harga=375000
    lama_pinjam = int(input("Masukkan lama pinjaman(dalam hitungan hari): "))
    total =harga*lama_pinjam
    print("Total harga yang harus dibayar : Rp. ",total)
elif merk_mobil == 'civic':
    print("Harga sewa = Rp 525.000/hari") 
    harga=525000
    lama_pinjam = int(input("Masukkan lama pinjaman(dalam hitungan hari): "))
    total1 =harga*lama_pinjam
    asuransi =total1*0.1
    total =total1+asuransi
    print("Total harga yang harus dibayar : Rp. ",total)  
else:
    print("Pilihan Mobil Tidak Tersedia")       
print()
print("Terima Kasih", nama, "sudah menggunakan layanan kami") 


