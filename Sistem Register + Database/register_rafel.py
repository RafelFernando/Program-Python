def register():
    print("-------------------")
    print("SILAHKAN REGISTRASI")
    print("-------------------")
    while True:
        nama = input("Nama: ")
        id = input("ID: ")
        if id.isdigit() and len(id) == 5:
          break         
        else:
            print("ID tidak sesuai ketentuan")
    with open("database.txt", "a") as data:
        data.write(f"{nama},{id}\n")

    print("REGISTRASI Sukses")   

def login():
    print("-------------")
    print("LOGIN CHECKER")
    print("-------------")
    with open("database.txt", "r") as data:
        user = data.readlines()
    gagal = 0
    while gagal <3:
        nama = input("Login Nama: ")
        id = input("Login ID: ")
        for datapenuh in user:
            data_pengguna = datapenuh.strip().split(",")
            if data_pengguna[0] == nama and data_pengguna[1] == id:
                print("LOGIN sukses")  
                return
        print("Gagal, coba lagi")
        gagal += 1
    print("Akun Terblokir")

pilih = input("Masukkan pilihan: ")
if pilih == "login":
    login()
else:
    register()


