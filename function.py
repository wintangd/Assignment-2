def daftar_kontak(kontak):
    for x in kontak:
        print("Daftar Kontak")
        print(f"Nama : {x['Nama']}")
        print(f"No. Telepon : {x['Telepon']}")

def tambah_kontak():
    Nama = input("Nama : ")
    Telepon = input("No. Telepon : ")
    x = {
        "Nama" : Nama,
        "No. Telepon" : Telepon
    }
    return x