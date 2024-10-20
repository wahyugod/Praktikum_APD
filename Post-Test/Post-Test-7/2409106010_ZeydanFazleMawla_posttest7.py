# Variabel Global
user = {
    "kominfo": {"password": "admin#1234", "role": "admin"}
}
produk_laptop = {}
jumlah_produk = 0

# Fungsi Rekursif Menghitung Total Harga
def hitung_total_harga(index=0, total=0):
    if index >= len(produk_laptop):
        return total
    harga = list(produk_laptop.values())[index]['harga']
    return hitung_total_harga(index + 1, total + int(harga))

# Fungsi login
def login(username, password):
    if username in user and user[username]["password"] == password:
        print(f"Masuk berhasil! Selamat datang, {username} (Role: {user[username]['role']})")
        return user[username]["role"]
    else:
        print("Username atau Password Salah!")
        return None

# Fungsi Tampilkan Produk
def tampilkan_produk():
    global jumlah_produk
    if len(produk_laptop) == 0:
        print("Produk Kosong!")
    else:
        for key, value in produk_laptop.items():
            print(f"\nNama Laptop : {key}\nMerek : {value['merek']}\nHarga : Rp{value['harga']}")
        print(f"\nJumlah Produk: {jumlah_produk}")

# Prosedur Untuk Menambah Produk
def tambah_produk():
    global jumlah_produk
    nama_produk = input("Masukan Nama Laptop : ")
    merek = input("Masukan Merek Laptop : ")
    
    while True:
        try:
            harga = int(input("Masukan Harga : "))
            break
        except ValueError:
            print("Harga harus berupa angka!")

    produk_laptop[nama_produk] = {"merek": merek, "harga": harga}
    jumlah_produk += 1
    print(f"Produk {nama_produk} berhasil ditambahkan.")

# Prosedur Untuk Mengubah Produk
def ubah_produk():
    global jumlah_produk
    nama_lama = input("Masukan Nama Produk yang ingin diubah: ")
    if nama_lama in produk_laptop:
        try:
            nama_baru = input("Masukan Nama Baru : ")
            merek_baru = input("Masukan Merek Baru : ")
            harga_baru = int(input("Masukan Harga Baru : "))
            produk_laptop[nama_baru] = {"merek": merek_baru, "harga": harga_baru}
            if nama_lama != nama_baru:
                del produk_laptop[nama_lama]
        except ValueError:
            print("Harga harus berupa angka!")
    else:
        print("Nama Tidak Ditemukan!")
        
# Prosedur Hapus Produk
def hapus_produk():
    global jumlah_produk
    if len(produk_laptop) == 0:
        print("Tidak Ada Produk Yang Dapat Dihapus!")
    else:
        nama_lama = input("Masukan Nama Yang Ingin Dihapus : ")
        if nama_lama in produk_laptop:
            del produk_laptop[nama_lama]
            jumlah_produk -= 1
            print(f"Produk {nama_lama} berhasil dihapus.")
        else:
            print("Nama Tidak ditemukan!")

# Fungsi Total Harga
def tampilkan_total_harga():
    total = hitung_total_harga()
    print(f"Total Harga Semua Produk: Rp{total}")

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

        role = login(username, password)

        # Program Utama CRUD
        if role:
            print("\n=================================")
            print("|    Toko Laptop Wahyu Jaya     |")
            print("=================================")
            print("| 1. Tampilkan Produk           |")
            if role == "admin":
                print("| 2. Tambah Produk              |")
                print("| 3. Ubah Produk                |")
                print("| 4. Hapus Produk               |")
            print("| 5. Tampilkan Total Harga      |")
            print("| 6. Keluar                     |")
            print("=================================")

            while True:
                pilih = input("\nMasukan Pilihan : ")
                if pilih == "1":
                    tampilkan_produk()

                elif pilih == "2" and role == "admin":
                    tambah_produk()

                elif pilih == "3" and role == "admin":
                    ubah_produk()

                elif pilih == "4" and role == "admin":
                    hapus_produk()

                elif pilih == "5":
                    tampilkan_total_harga()

                elif pilih == "6":
                    print("Terima Kasih Telah Melihat Produk Kami")
                    break

                else:
                    print("Pilihan Tidak Valid!")

    # Register Hanya Untuk Pengunjung
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