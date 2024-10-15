import os

os.system('cls || clear')

akun = {"admin":"admin"}

data_parfum = []


while True:
    os.system('cls || clear')
    print("="*40)
    print("MENU UTAMA".center(40))
    print("="*40)
    print("[1] LOGIN")
    print("[2] BUAT AKUN")
    print("[3] EXIT")
    pilihan = input("\nMasukkan Pilihan = ")

    if pilihan == "1":
        batas_login = 3
        is_login = False
        while batas_login > 0:
            os.system('cls || clear')
            print("="*40)
            print("MAIN MENU".center(40))
            print("="*40)

            username = input("masukkan username: ")
            password = input("masukkan password: ")

            if username in akun and akun[username] == password:
                is_login = True
                usersaatini = username
                os.system('cls || clear')
                print(f"\nBerhasil Login!")
                input("\nKlik enter untuk menlanjutkan...")
                break
            batas_login -= 1
            print("\nID atau PASSWORD salah!")
            input("\nKlik enter untuk menlanjutkan...")

        if is_login:
            while is_login:
                os.system('cls || clear')
                print("="*40)
                print("PARFUM WANGI WANGI".center(40))
                print("="*40)

                if usersaatini == "admin":
                    print("[1] tambah parfum")
                    print("[2] hapus list parfum")
                print("[3] list parfum")
                print("[4] log out")
                print("[5] Exit")
                pilihan = input("\nMasukkan Pilihan: ")

                if pilihan == "1" and usersaatini == "admin":
                    os.system('cls || clear')
                    print("="*40)
                    print("MASUKKAN DATA PARFUM".center(40))
                    print("="*40)
                    nama_parfum = input("masukkan nama parfum: ")
                    jumlah = int (input("masukkan jumlah parfum: "))
                    harga = float (input("masukkan harga: "))
                    data_parfum.append([nama_parfum, jumlah, harga])
                    print("Data parfum berhasil ditambah")
                    input("\nklik enter untuk melanjutkan...")

                elif pilihan == "2" and usersaatini == "admin":
                    os.system('cls || clear')
                    print("="*40)
                    print("HAPUS DATA PARFUM".center(40))
                    print("="*40)
                    for i, parfum in enumerate(data_parfum):
                        print(f"{i+1}\t {parfum[0]}\t\t\t{parfum[1]}\t\t\t{parfum[2]:,.2f}")
                    hapus_pilih = int (input("masukkan nomor parfum yang ingin di hapus: ")) -1
                    if 0 <= hapus_pilih < len(data_parfum):
                        data_parfum.pop(hapus_pilih)
                        print("parfum berhasil di hapus")
                    else:
                        print("nomor parfum tidak valid")
                    input("\nKlik enter untuk melanjutkan...")

                elif pilihan == "3":
                    os.system('cls || clear')
                    print("="*70)
                    print("LIST PARFUM ".center(70))
                    print("="*70)
                    print("NO. | \t Nama Parfum\t |\tJumlah \t\t|\tHarga")
                    for i, parfum in enumerate(data_parfum):
                        print(f"{i+1}\t {parfum[0]}\t\t\t{parfum[1]}\t\t\t{parfum[2]:,.2f}")
                    input("\nKlik enter untuk menlanjutkan...")

                elif pilihan == "4":
                    break

                elif pilihan == "5":
                    os.system('cls || clear')
                    print("="*40)
                    print("TERIMAKASIH".center(40))
                    print("="*40)
                    exit()

                else:
                    print("\nPilihan tidak tersedia! atau anda tidak memiliki akses")
                    input("\nKlik enter untuk menlanjutkan...")

            continue
        else:
            print("\nGagal Login! PROGRAM BERHENTI")
            input("\nKlik enter untuk menlanjutkan...")
            is_login = False
            break

    elif pilihan == "2":
        os.system('cls || clear')
        print("="*40)
        print("SILAHKAN BUAT AKUN".center(40))
        print("="*40)
        username = input("username baru\t: ")
        if username in akun:
            print("username sudah ada!")
        else:
            password = input("password baru\t: ")
            akun[username] = password
            print("akun berhasil dibuat!")
        input("\nKlik enter untuk menlanjutkan...")

    elif pilihan == "3":
        os.system('cls || clear')
        print("="*40)
        print("TERIMAKASIH".center(40))
        print("="*40)
        is_login = False
        break

    else:
        print("maaf pilihan tidak ada")
        input("\nKlik enter untuk menlanjutkan...")
        continue
