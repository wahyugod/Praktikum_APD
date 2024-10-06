# CRUD Manajemen Produk Laptop Toko Wahyu Jaya

# Format username, password, role
user = [["kominfo", "admin#1234", "admin"]]
produk_laptop = []

# Sesi Login
while True:
    print("\n=================================")
    print("|    Toko Laptop Wahyu Jaya     |")
    print("=================================")
    print("| 1. Login                      |")
    print("| 2. Register                   |")
    print("| 3. Keluar                     |")
    print("=================================")
    pilihan = input("Masukan Pilihan : ")

    if pilihan == "1":
        username = input("\nMasukkan Username : ")
        password = input("Masukkan Password : ")
        masuk = False

        for akun in user:
            if akun[0] == username and akun[1] == password:
                print(f"Masuk berhasil! Selamat datang, {username} (Role: {akun[2]})")
                masuk = True
                role = akun[2]
                break
        else:
            print("Username atau Password Salah!")

        # Program Utama CRUD
        if masuk:
            print("\n=================================")
            print("|    Toko Laptop Wahyu Jaya     |")
            print("=================================")
            print("| 1. Tampilkan Produk           |")
            if role == "admin":
                print("| 2. Tambah Produk              |")
                print("| 3. Ubah Produk                |")
                print("| 4. Hapus Produk               |")
            print("| 5. Keluar                     |")
            print("=================================")

            while True:
                pilih = input("\nMasukan Pilihan : ")
                if pilih == "1":
                    if len(produk_laptop) == 0:
                        print("Produk Kosong!")
                    else:
                        for i in range(len(produk_laptop)):
                            print(f"\nProduk Laptop Ke-{i+1}\nNama Laptop : {produk_laptop[i][0]}\nMerek : {produk_laptop[i][1]}\nHarga : Rp{produk_laptop[i][2]}")
                elif pilih == "2" and role == "admin":
                    nama_produk = input("Masukan Nama Laptop : ")
                    merek = input("Masukan Merek Laptop : ")
                    harga = input("Masukan Harga : ")
                    produk_laptop.append([nama_produk,merek,harga])
                elif pilih == "3" and role == "admin":
                    nama_lama = input("Masukan Nama Yang Ingin Diganti : ")
                    for i in range(len(produk_laptop)):
                        if produk_laptop[i][0] == nama_lama:
                            nama_baru = input("\nMasukan Nama Baru : ")
                            merek_baru = input("Masukan Merek Baru : ")
                            harga_baru = input("Masukan Harga Baru : ")
                            produk_laptop[i][0] = nama_baru
                            produk_laptop[i][1] = merek_baru
                            produk_laptop[i][2] = harga_baru
                            break
                    else:
                        print("Nama Tidak ditemukan!")
                elif pilih == "4" and role == "admin":
                    if len(produk_laptop) == 0:
                        print("Tidak Ada Produk Yang Dapat Dihapus!")
                    else:
                        nama_lama = input("Masukan Nama Yang Ingin Dihapus : ")
                        for i in range(len(produk_laptop)):
                            if produk_laptop[i][0] == nama_lama:
                                del produk_laptop[i]
                                break
                        else:
                            print("Nama Tidak ditemukan!")
                elif pilih == "5":
                    print("Terima Kasih Telah Melihat Produk Kami")
                    break
                else:
                    print("Pilihan Tidak Valid!")

    elif pilihan == "2":
        username_baru = input("Masukkan Username Baru : ")
        password_baru = input("Masukkan Password Baru : ")

        # Pengecekan Nama Pengguna
        pengguna_terdaftar = False
        for akun in user:
            if akun[0] == username_baru:
                pengguna_terdaftar = True
                break

        if pengguna_terdaftar:
            print("Nama Pengguna Sudah Terdaftar!")

        else:
            role_baru = "pengunjung"
            user.append([username_baru, password_baru, role_baru])
            print(f"Pendaftaran Berhasil Untuk {username_baru} Dengan Role {role_baru}!")

    # Keluar
    elif pilihan == "3":
        print("Terima Kasih Telah Berkunjung.")
        break

    else:
        print("Pilihan Tidak Valid!")