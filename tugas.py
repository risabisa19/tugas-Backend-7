# program management kontak
import function
daftar_kontak = []
daftar_kontak.append ({
    "nama" : "kharisma" ,
    "email" : "kharisma@gmail.com" ,
    "telepon" : "089623568964"
})
#menu program
while True:
    print ("menu pilihan")
    print("1. Daftar kontak")
    print("2. Tambah kontak")
    print("3. Hapus kontak")
    print("4. Cari kontak")
    print("0. Program exit")

    menu = input("silahkan pilih : ")
    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3" :
        function.hapus_kontak(daftar_kontak)    
    elif menu ==  "4" :
        function.cari_kontak(daftar_kontak)    
    else :
        print("menu tidak tersedia")    
print("program berjalan dengan baik")    
     