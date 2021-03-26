import function

kontak = []
kontak.append({
    "Nama" : "Wintang",
    "Telepon" : "081373553022"
})

while True:
    print("Selamat Datang!")
    print("--Menu--")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    menu = input("Pilih Menu : ")
    if menu == "3":
        break
    elif menu == "2":
        x = function.tambah_kontak()
        kontak.append(x)
    elif menu == "1":
        function.daftar_kontak(kontak)
    else:
        print("Menu tidak tersedia")

print("Program selesai, sampai jumpa!") 