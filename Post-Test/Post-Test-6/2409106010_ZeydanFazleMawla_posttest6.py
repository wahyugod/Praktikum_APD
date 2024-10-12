# CRUD Manajemen Produk Laptop Toko Wahyu Jaya Menggunakan Dictionary

# Format {username: {password, role}}
# Register Hanya Untuk Pengunjung

user = {
    "kominfo": {"password": "admin#1234", "role": "admin"}
}
produk_laptop = {}

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

        if username in user and user[username]["password"] == password:
            print(f"Masuk berhasil! Selamat datang, {username} (Role: {user[username]['role']})")
            role = user[username]["role"]

            # Program Utama CRUD
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
                        for key, value in produk_laptop.items():
                            print(f"\nNama Laptop : {key}\nMerek : {value['merek']}\nHarga : Rp{value['harga']}")
                elif pilih == "2" and role == "admin":
                    nama_produk = input("Masukan Nama Laptop : ")
                    merek = input("Masukan Merek Laptop : ")
                    harga = input("Masukan Harga : ")
                    produk_laptop[nama_produk] = {"merek": merek, "harga": harga}
                elif pilih == "3" and role == "admin":
                    nama_lama = input("Masukan Nama Yang Ingin Diganti : ")
                    if nama_lama in produk_laptop:
                        nama_baru = input("\nMasukan Nama Baru : ")
                        merek_baru = input("Masukan Merek Baru : ")
                        harga_baru = input("Masukan Harga Baru : ")
                        produk_laptop[nama_baru] = {"merek": merek_baru, "harga": harga_baru}
                        if nama_lama != nama_baru:
                            del produk_laptop[nama_lama]
                    else:
                        print("Nama Tidak ditemukan!")
                elif pilih == "4" and role == "admin":
                    if len(produk_laptop) == 0:
                        print("Tidak Ada Produk Yang Dapat Dihapus!")
                    else:
                        nama_lama = input("Masukan Nama Yang Ingin Dihapus : ")
                        if nama_lama in produk_laptop:
                            del produk_laptop[nama_lama]
                        else:
                            print("Nama Tidak ditemukan!")
                elif pilih == "5":
                    print("Terima Kasih Telah Melihat Produk Kami")
                    break
                else:
                    print("Pilihan Tidak Valid!")

        else:
            print("Username atau Password Salah!")

    elif pilihan == "2":
        username_baru = input("Masukkan Username Baru : ")
        password_baru = input("Masukkan Password Baru : ")

        # Pengecekan Nama Pengguna
        if username_baru in user:
            print("Nama Pengguna Sudah Terdaftar!")
        else:
            role_baru = "pengunjung"
            user[username_baru] = {"password": password_baru, "role": role_baru}
            print(f"Pendaftaran Berhasil Untuk {username_baru} Dengan Role {role_baru}!")

    # Keluar
    elif pilihan == "3":
        print("Terima Kasih Telah Berkunjung.")
        break

    else:
        print("Pilihan Tidak Valid!")