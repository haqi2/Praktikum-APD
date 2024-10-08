akuns = []
penjualan_parfum = []

while True:
    print("Halo! selamat datang di pendataan parfum")
    print("Silakan pilih 'Daftar akun' jika belum buat akun, dan jika sudah memiliki akun silahkan 'Login'")
    print("1. Daftar akun")
    print("2. Login")
    print("3. Exit")
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username:  
                akuna = True
                break
        if akuna:
            print("Nama Sudah Terpakai Untuk Registrasi Silahkan Coba Lagi")
        else:
            Password = input("Password: ")
            akuns.append([Username, Password, []])  
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")
 

    elif opsi == "2":
        print("Hi, Silahkan login dulu ya!")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akuns:
            if akun[0] == Username and akun[1] == Password: 
                while True:
                    print(f"\nSelamat datang {Username}!")
                    print("Menu:")
                    print("1. Tambah data penjualan parfum")
                    print("2. Tampilkan data penjualan parfum")
                    print("3. Ubah data penjualan parfum")
                    print("4. Hapus data penjualan parfum")
                    print("5. Keluar")
                
                    pilihan = input("Pilih menu (1/2/3/4/5): ")
                
                    if pilihan == "1":
                        nama_parfum = input("Masukkan nama parfum: ")
                        jumlah = input("Masukkan jumlah parfum: ")
                        harga = input("Masukkan harga parfum: ")
                
                        if int(jumlah) and (float(harga) or int(harga)):
                            penjualan_parfum.append([nama_parfum, int(jumlah), float(harga)])
                            print("Data berhasil ditambahkan.")
                        else:
                            print("Input jumlah atau harga tidak valid. Pastikan jumlah berupa angka bulat dan harga berupa angka desimal.")
                
                    elif pilihan == "2":
                        if len(penjualan_parfum) == 0:
                            print("Belum ada data penjualan parfum.")
                        else:
                            print("Data penjualan parfum:")
                            for i in range(len(penjualan_parfum)):
                                print(f"{i+1}. Nama: {penjualan_parfum[i][0]}, Jumlah: {penjualan_parfum[i][1]}, Harga: {penjualan_parfum[i][2]:,.2f}")
                    
                    elif pilihan == "3":
                        if len(penjualan_parfum) == 0:
                            print("Belum ada data untuk diubah.")
                        else:
                            for i in range(len(penjualan_parfum)):
                                print(f"{i+1}. Nama: {penjualan_parfum[i][0]}, Jumlah: {penjualan_parfum[i][1]}, Harga: {penjualan_parfum[i][2]:,.2f}")
                
                            index = input("Masukkan nomor urutan parfum yang ingin diubah: ")
                
                            if int(index) and 0 < int(index) <= len(penjualan_parfum):
                                index = int(index) - 1
                                nama_baru = input("Masukkan nama parfum baru: ")
                                jumlah_baru = input("Masukkan jumlah baru: ")
                                harga_baru = input("Masukkan harga baru: ")
                
                                if int(jumlah_baru) and (float(harga_baru) or int(harga_baru)):
                                    penjualan_parfum[index] = [nama_baru, int(jumlah_baru), float(harga_baru)]
                                    print("Data berhasil diubah.")
                                else:
                                    print("Input jumlah atau harga tidak valid. Pastikan jumlah berupa angka bulat dan harga berupa angka desimal.")
                            else:
                                print("Nomor urutan tidak valid.")
                    
                    elif pilihan == "4":
                        if len(penjualan_parfum) == 0:
                            print("Belum ada data untuk dihapus.")
                        else:
                            for i in range(len(penjualan_parfum)):
                                print(f"{i+1}. Nama: {penjualan_parfum[i][0]}, Jumlah: {penjualan_parfum[i][1]}, Harga: {penjualan_parfum[i][2]:,.2f}")
                
                            index = input("Masukkan nomor urutan parfum yang ingin dihapus: ")
                
                            if int(index) and 0 < int(index) <= len(penjualan_parfum):
                                index = int(index) - 1
                                del penjualan_parfum[index]
                                print("Data berhasil dihapus.")
                            else:
                                print("Nomor urutan tidak valid.")
                    
                    elif pilihan == "5":
                        print("Program selesai.")
                        break
                    
                    else:
                        print("Pilihan tidak valid. Coba lagi.")
                break
        else:
            print("Username dan password anda salah, silahkan coba lagi\n")

    elif opsi == "3":
        print("Apakah kamu yakin ingin keluar dari pendataan parfum? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah mau mendata parfum, semoga harimu menyenangkan!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")