#variabel
total = 0
makanan = []
harga = []

while True:
#melakukan perulangan sencara terus menerus hingga kondisinya bernilai false
    print (" SELAMAT DATANG DI WARUNG ROZAK")
    print("         --- MENU ---        ")
    print("1.         Soto Ayam          | Rp 13000")
    print("2.         Soto Daging        | Rp 16000")
    print("3.         Betawi Daging      | Rp 20000")
    print("4.         Betawi Kambing     | Rp 20000")
    print("5.         Es Teh             | Rp 3000 ")
    print("6.         Es Jeruk           | Rp 5000 ")
    print("         --- MENU ---        ")
#print mencetak string
    kode = int(input("masukkan kode menu makanan : "))
    if kode ==1:
        makanan.append('Soto Ayam')
        harga.append(13000)
        total += 13000
    elif kode ==2:
        makanan.append('Soto Daging')
        harga.append(16000)
        total += 16000
    elif kode ==3:
        makanan.append('Betawi Daging')
        harga.append(20000)
        total += 20000
    elif kode ==4:
        makanan.append('Betawi Kambing')
        harga.append(20000)
        total += 20000
    elif kode ==5:
        makanan.append('Es Teh')
        harga.append(3000)
        total += 3000
    elif kode ==6:
        makanan.append('Es Jeruk')
        harga.append(6000)
        total += 6000
    else:
        print("Kode menu makanan tidak terdaftar")
        
    lanjut = input('lanjut benlaja (y/t) : ')
    if lanjut == 't':
        print("")
        break
    # break untuk menghentikan perulangan jika tidak dihentikan maka akan terjadi perulangan trus menerus
    
    
print ('makanan yang dibeli :', makanan)    
print ('harga makanannya :', harga)
print ('total yang harus dibayar :', total, '\n')

uang = int(input('masukkan uang pembayaran :'))
if uang > total:
    print('kembaliannya :', uang - total)
elif uang == total:
    print('uang pas')
else:
    print('uang kurang', uang - total)