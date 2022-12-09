nama = input("Masukkan nama : ")
jumlah = 0

for i in range(len(nama)):
    jumlah += 1
    print(nama[0:jumlah])
for j in range(len(nama)):
    jumlah -=  1
    print(nama[0:jumlah])
     
    
