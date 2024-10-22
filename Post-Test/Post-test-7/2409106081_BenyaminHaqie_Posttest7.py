import os
akun = {"admin":"admin"}
data_parfum = {}

def clear():
    os.system('cls || clear')

def main_menu():
    clear()
    print("="*40)
    print("MAIN MENU".center(40))
    print("="*40)
    print("[1] LOGIN")
    print("[2] BUAT AKUN")
    print("[3] EXIT")

def admin_menu():
    clear()
    print("="*40)
    print("PARFUM WANGI WANGI".center(40))
    print("="*40)
    print("[1] Tambah Parfum")
    print("[2] Hapus data parfum")
    print("[3] List Parfum")
    print("[4] Log Out")
    print("[5] Exit")

def user_menu():
    clear()
    print("="*40)
    print("PARFUM WANGY WANGY".center(40))
    print("="*40)
    print("[3] List Parfum")
    print("[4] Log Out")
    print("[5] Exit")

def login(user_akun):
    clear()
    batas_login = 3
    while batas_login > 0:
        clear()
        print("="*40)
        print("MAIN MENU".center(40))
        print("="*40)
        username = input("USERNAME\t: ")
        password = input("PASSWORD\t: ")
        if username in user_akun and user_akun[username] == password:
            clear()
            print(f"\nBerhasil Login! anda login sebagai {username}")
            input("\nKlik enter untuk menlanjutkan...")
            return True, username
        batas_login -= 1
        print("\nTerjadi Kesalahan Pada Data Login!")
        print(f"\nKesempatan login tersisa {batas_login} kali lagi!")
        input("\nKlik enter untuk menlanjutkan...")
        clear()
    print("\nMohon maaf anda sudah salah 3 kali, Silahkan coba lagi nanti")###########
    exit()

def bikin_akun(user_akun):
    clear()
    print("="*40)
    print("BUAT AKUN DULU!".center(40))
    print("="*40)
    username = input("Masukkan Username\t: ")
    if username in user_akun:
        print("Username Telah Dipakai!")
    else:
        password = input("Masukkan Password\t: ")
        akun[username] = password
        print("AKUN TELAH JADI SILAHKAN LOGIN!")
    input("\nKlik enter untuk menlanjutkan...")

def tambah_parfum(data_parfum):
    clear()
    print("="*40)
    print("MENU PARFUM".center(40))
    print("="*40)
    nama_parfum = input("Nama Parfum: ")
    jumlah = int(input("Masukkan jumlah parfum: "))
    harga = float(input("Masukkan harga: "))

    if nama_parfum in data_parfum:
        data_parfum[nama_parfum]['jumlah'] += jumlah
        data_parfum[nama_parfum]['harga'] = harga
    else:
        data_parfum[nama_parfum] = {'jumlah': jumlah, 'harga': harga}

    print("\nParfum berhasil ditambahkan!")
    input("\nKlik enter untuk menlanjutkan...")

def list_parfum():
    clear()
    print("LIST PARFUM".center(30))
    print("="*30)
    if not data_parfum:
        print("Tidak ada data parfum.")
    else:
        for nama, info in data_parfum.items():
            print(f"Nama: {nama}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")
    input("\nKlik enter untuk melanjutkan...")

def hapus_parfum():
    clear()
    print("="*40)
    print("DATA PARFUM YANG TELAH TERPAKAI".center(40))
    print("="*40)
    for nama, info in data_parfum.items():
        print(f"Nama: {nama}, Jumlah: {info['jumlah']}, Harga: {info['harga']}")

    nama_parfum = input("\nNama Parfum yang akan dihapus: ")
    if nama_parfum in data_parfum:
        del data_parfum[nama_parfum]
        print(f"Parfum {nama_parfum} berhasil dihapus.")
    else:
        print(f"Parfum {nama_parfum} tidak ditemukan.")


IS_LOGIN = False
while True:
    clear()
    main_menu()
    pilihan = input("\nMasukkan Pilihan: ")
    if pilihan == "1":
        IS_LOGIN, usersekarang = login(akun)
        if IS_LOGIN:
            while IS_LOGIN:
                clear()
                if usersekarang == "admin":
                    admin_menu()
                else:
                    user_menu()
                pilihan = input("\nMasukkan pilihan: ")

                if pilihan == "1" and usersekarang == "admin":
                    tambah_parfum(data_parfum)

                elif pilihan == "2" and usersekarang == "admin":
                    hapus_parfum()

                elif pilihan == "3":
                    list_parfum()

                elif pilihan == "4":
                    IS_LOGIN = False

                elif pilihan == "5":
                    exit()

    elif pilihan == "2":
        bikin_akun(akun)

    elif pilihan == "3":
        IS_LOGIN = False
        clear()
        break

    else:
        print("PILIHAN TIDAK ADA")
        input("\nKlik enter untuk menlanjutkan...")
        continue
    