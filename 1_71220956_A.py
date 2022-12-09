deret_awal = int(input("Masukkan awal deret : "))
deret_akhir = int(input("Masukkan akhir deret : "))

for i in range(deret_awal, deret_akhir):
    if i%3!= 0 and i%6 != 0 and i%2!=0:
        print(i, end=' ')
