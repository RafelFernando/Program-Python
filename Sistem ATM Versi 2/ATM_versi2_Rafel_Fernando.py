data_pengguna = {
    'Rafel Fernando': {'pin': 'rafel123', 'saldo': 20000000},
    'Enda Afiandika': {'pin': 'enda123', 'saldo': 100000000}
}

def login():
    username = input("Masukkan username: ")
    pin = input("Masukkan PIN: ")

    if username in data_pengguna and pin == data_pengguna[username]['pin']:
        print("Login berhasil")
        return True
    else:
        print("Login gagal. Cek kembali username dan PIN Anda.")
        return False

def cek_saldo(username):
    saldo = data_pengguna[username]['saldo']
    print(f"Saldo Anda saat ini: Rp {saldo}")

def tarik_tunai(username):
    nominal = int(input("Masukkan nominal yang ingin ditarik: Rp "))
    if nominal > 0 and nominal <= data_pengguna[username]['saldo']:
        data_pengguna[username]['saldo'] -= nominal
        print(f"Tarik tunai berhasil. Saldo Anda saat ini: Rp {data_pengguna[username]['saldo']}")
    else:
        print("Tarik tunai gagal. Saldo tidak mencukupi atau nominal tidak valid.")

def transfer(username):
    tujuan_transfer = input("Masukkan username penerima transfer: ")
    if tujuan_transfer in data_pengguna:
        nominal_transfer = int(input("Masukkan nominal yang ingin ditransfer: Rp "))
        if nominal_transfer > 0 and nominal_transfer <= data_pengguna[username]['saldo']:
            data_pengguna[username]['saldo'] -= nominal_transfer
            data_pengguna[tujuan_transfer]['saldo'] += nominal_transfer
            print(f"Transfer berhasil. Saldo Anda saat ini: Rp {data_pengguna[username]['saldo']}")
        else:
            print("Transfer gagal. Saldo tidak mencukupi atau nominal tidak valid.")
    else:
        print("Username penerima transfer tidak valid.")

while True:
    print("=============================")
    print("=== Selamat Datang di ATM ===")
    print("=============================")
    if login():
        username = input("Masukkan username: ")
        while True:
            print("\nMenu:")
            print("1. Cek Saldo")
            print("2. Tarik Tunai")
            print("3. Transfer")
            print("4. Keluar")

            pilihan = input("Masukkan pilihan Anda (1-4): ")

            if pilihan == '1':
                cek_saldo(username)
            elif pilihan == '2':
                tarik_tunai(username)
            elif pilihan == '3':
                transfer(username)
            elif pilihan == '4':
                print("Terima kasih. Sampai jumpa lagi!")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")