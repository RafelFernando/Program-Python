print("============================")
print("=====Cek Bilangan Prima=====")
print("============================")

bilangan = int(input("Masukkan bilangan: "))

for i in range(2, bilangan):
    if (bilangan % i == 0):
        print(bilangan, "adalah bukan bilangan prima")
        break
else:
    print(bilangan, " adalah bilangan prima")



