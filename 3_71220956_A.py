angka = int(input("Masukkan Pembatas : "))
angka2 = int(input("Masukkan Angka yang dilarang : "))

for i in range(0,angka,1):
    if i == angka2:
        continue
    print(i,end=' ')
    

    
