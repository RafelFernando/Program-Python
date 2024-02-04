user_id = 0
loop = "y"
user = [
    {
        "id": "1234",
        "no_rekening": "1234567890",
        "username": "Bob Sadino",
        "pin": "2108",
        "saldo": 0
    },
    {
        "id": "4321",
        "no_rekening": "0987654321",
        "username": "Rafel Fernando",
        "pin": "1234",
        "saldo": 250000000
    }
]
status_login = False
pakai_atm = "y"


def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False


def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return i
    return -1


def cek_rekening(no):
    for i in range(len(user)):
        if str(user[i]['no_rekening']) == str(no):
            return i
    return -1


def transfer_uang(uang, no_rekening):
    index1 = cek_user(user_id)
    index2 = cek_rekening(no_rekening)
    if index1 >= 0 and index2 >= 0:
        uang = int(uang)
        if user[index1]['saldo'] >= uang:
            user[index1]['saldo'] -= uang
            user[index2]['saldo'] += uang
            print("Anda berhasil mentransfer uang Rp." + str(uang) + " ke Rekening " + no_rekening)
            print("Sisa saldo anda adalah Rp.", user[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")
    else:
        print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")


def ambil_uang(uang):
    index1 = cek_user(user_id)
    if index1 >= 0:
        uang = int(uang)
        if user[index1]['saldo'] >= uang:
            user[index1]['saldo'] -= uang
            print("Anda berhasil menarik uang Rp." + str(uang))
            print("Sisa saldo anda adalah Rp.", user[index1]['saldo'])
        else:
            print("Ops saldo anda tidak cukup")
    else:
        print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")


while pakai_atm == "y":
    while status_login == False:
        print("SELAMAT DATANG DI ATM BANK BCA")
        pin = input("Masukan PIN : ")
        cl = cek_login(pin)
        if cl != False:
            print("Selamat datang " + cl['username'])
            user_id = cl['id']
            status_login = True
        else:
            print("Ops PIN anda salah")
            
    print("")
    print("SELAMAT DATANG DI ATM BANK BCA")
    print("1. Cek Saldo")
    print("2. Transfer Uang")
    print("3. Ambil Uang")
    print("4. Logout")
    print("5. Keluar ATM")
    a = int(input("Silahkan pilih menu : "))

    if a == 1:
        print("Sisa Saldo anda adalah Rp.", user[cek_user(user_id)]['saldo'])
    elif a == 2:
        print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
        no_rek = input("Masukan No Rekening Tujuan: ")
        cnk = cek_rekening(no_rek)
        if cnk >= 0:
            print("Nomor rekening ditemukan, silahkan masukan nominal yang akan di transfer")
            nominal = input("Nominal Yang Akan Di Transfer: ")
            transfer_uang(nominal, no_rek)
        else:
            print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
    elif a == 3:
        nominal = input("Nominal Yang Akan Di Tarik : ")
        ambil_uang(nominal)
    elif a == 4:
        status_login = False
    elif a == 5:
        status_login = False
        loop = "n"
    else:
        pakai_atm = "n"
        print("Pilihan tidak tersedia")

    if status_login == True:
        input("Kembali ke menu (Enter) ")
        print("")
    loop = "y"