import csv
from tabulate import tabulate
import os
import time
import sys

# CRUD Manajemen Produk Laptop

user = {
    "admin": {"password": "admin", "role": "admin"}
}
produk_laptop = {}
data_pengunjung = []
produk_dibeli = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def loading(duration=5):
    animation = [
        "Loading .   ",
        "Loading ..  ",
        "Loading ... ",
        "Loading     "
    ]
    start_time = time.time()
    while time.time() - start_time < duration:
        for frame in animation:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(0.3)

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
    if len(produk_laptop) == 0:
        print("Produk Kosong!")
    else:
        # Mengonversi produk_laptop ke dalam list of lists agar mudah ditampilkan dengan tabulate
        tabel_data = [[nama, data['merek'], data['prosesor'], data['vga'], f"Rp{data['harga']}"] 
        for nama, data in produk_laptop.items()]
        print(tabulate(tabel_data, headers=["Nama", "Merek", "Prosesor", "VGA", "Harga"], tablefmt="grid"))

# Prosedur Untuk Menambah Produk
def tambah_produk():
    nama_produk = input("Masukan Nama Laptop : ")
    if nama_produk in produk_laptop:
        print(f"Produk Dengan Nama '{nama_produk}' Sudah Ada!")
        return

    merek = input("Masukan Merek Laptop : ")
    prosesor = input("Masukan Prosesor Laptop : ")
    vga = input("Masukan VGA Laptop : ")

    while True:
        try:
            harga = int(input("Masukan Harga : "))
            break
        except ValueError:
            print("Harga harus berupa angka!")

    produk_laptop[nama_produk] = {
        "merek": merek,
        "prosesor": prosesor,
        "vga": vga,
        "harga": harga
    }
    simpan_data_csv()
    print(f"Produk {nama_produk} berhasil ditambahkan.")

# Prosedur Untuk Mengubah Produk
def ubah_produk():
    tampilkan_produk()
    nama_lama = input("Masukan Nama Produk yang ingin diubah: ")

    if nama_lama in produk_laptop:
        try:
            nama_baru = input("Masukan Nama Baru : ")
            merek_baru = input("Masukan Merek Baru : ")
            prosesor_baru = input("Masukan Prosesor Baru : ")
            vga_baru = input("Masukan VGA Baru : ")
            harga_baru = int(input("Masukan Harga Baru : "))

            produk_laptop[nama_baru] = {
                "merek": merek_baru,
                "prosesor": prosesor_baru,
                "vga": vga_baru,
                "harga": harga_baru
            }

            if nama_lama != nama_baru:
                del produk_laptop[nama_lama]
            simpan_data_csv()
            print("Produk Berhasil Diubah!")

        except ValueError:
            print("Harga Harus Berupa Angka!")
    else:
        print("Nama Tidak Ditemukan!")
        
# Prosedur Hapus Produk
def hapus_produk():
    tampilkan_produk()
    if len(produk_laptop) == 0:
        print("Tidak Ada Produk Yang Dapat Dihapus!")
    else:
        nama_lama = input("Masukan Nama Yang Ingin Dihapus : ")
        if nama_lama in produk_laptop:
            del produk_laptop[nama_lama]
            simpan_data_csv()
            print(f"Produk {nama_lama} berhasil dihapus.")
        else:
            print("Nama Tidak ditemukan!")

def beli_produk(username):
    if len(produk_laptop) == 0:
        print("Tidak ada produk yang tersedia untuk dibeli.")
    else:
        tampilkan_produk()
        nama_produk = input("Masukkan nama produk yang ingin dibeli: ")
        if nama_produk in produk_laptop:
            produk_dibeli.append(produk_laptop[nama_produk])  # Tambah ke daftar umum produk_dibeli
            user[username]["produk_dibeli"].append(nama_produk)  # Tambahkan nama produk ke produk_dibeli user
            del produk_laptop[nama_produk]
            simpan_data_csv()
            print(f"Produk '{nama_produk}' berhasil dibeli dan dihapus dari daftar produk.")
        else:
            print("Produk tidak ditemukan!")

# Fungsi Total Harga
def tampilkan_total_harga():
    total = hitung_total_harga()
    print(f"Total Harga Semua Produk: Rp{total}")

# Fungsi Simpan Data ke CSV
def simpan_data_csv():
    with open('data_produk.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Merek", "Prosesor", "VGA", "Harga"])
        for nama, data in produk_laptop.items():
            writer.writerow([nama, data["merek"], data["prosesor"], data["vga"], data["harga"]])

# Fungsi Muat Data dari CSV
def muat_data_csv():
    try:
        with open('data_produk.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                produk_laptop[row["Nama"]] = {
                    "merek": row["Merek"],
                    "prosesor": row["Prosesor"],
                    "vga": row["VGA"],
                    "harga": int(row["Harga"])
                }
    except FileNotFoundError:
        print("File data_produk.csv tidak ditemukan, mulai dengan data kosong.")

def user_register():
    username_baru = input("Masukkan Username Baru : ")
    password_baru = input("Masukkan Password Baru : ")

    if username_baru in user:
        print("Nama Pengguna Sudah Terdaftar!")
    else:
        role_baru = "pengunjung"
        user[username_baru] = {"password": password_baru, "role": role_baru, "produk_dibeli": []}
        data_pengunjung.append({"username": username_baru, "password": password_baru})
        print(f"Pendaftaran Berhasil Untuk {username_baru} Dengan Role {role_baru}!")

# Fungsi untuk Menampilkan Data User (Pengunjung)
def tampilkan_data_user():
    if len(user) == 0:
        print("Tidak ada pengunjung yang terdaftar.")
    else:
        print("\nBerikut Adalah Data Pengunjung")
        tabel_data = []
        for username, data in user.items():
            if data["role"] == "pengunjung":
                produk_dibeli = ", ".join(data["produk_dibeli"]) if data["produk_dibeli"] else "Tidak ada"
                tabel_data.append([username, data['password'], produk_dibeli])
        
        print(tabulate(tabel_data, headers=["Username", "Password", "Produk Dibeli"], tablefmt="grid"))

def login_menu():
    print("\n=================================")
    print("|    Toko Laptop Wahyu Jaya     |")
    print("=================================")
    print("| 1. Login                      |")
    print("| 2. Register                   |")
    print("| 3. Keluar                     |")
    print("=================================")

def main_menu():
    if role == "admin":
        print("\n=================================")
        print("|    Toko Laptop Wahyu Jaya     |")
        print("=================================")
        print("| 1. Tampilkan Produk           |")
        print("| 2. Tambah Produk              |")
        print("| 3. Ubah Produk                |")
        print("| 4. Hapus Produk               |")
        print("| 5. Tampilkan Total Harga      |")
        print("| 6. Tampilkan Data User        |")
        print("| 7. Keluar                     |")
        print("=================================")
    else:
        print("\n=================================")
        print("|    Toko Laptop Wahyu Jaya     |")
        print("=================================")
        print("| 1. Tampilkan Produk           |")
        print("| 4. Beli Produk                |")
        print("| 5. Tampilkan Total Harga      |")
        print("| 7. Keluar                     |")
        print("=================================")

def back():
    input("Tekan Enter Untuk Melanjutkan...")

# Sesi Login
muat_data_csv()
while True:
    clear()
    login_menu()
    pilihan = input("Masukan Pilihan : ")
    clear()

    if pilihan == "1":
        username = input("\nMasukkan Username : ")
        password = input("Masukkan Password : ")
        role = login(username, password)
        back()
        clear()

        # Program Utama CRUD
        if role:
            while True:
                main_menu()
                pilih = input("Masukan Pilihan : ")
                clear()

                if pilih == "1":
                    tampilkan_produk()
                    back()
                    clear()

                elif pilih == "2" and role == "admin":
                    tambah_produk()
                    back()
                    clear()

                elif pilih == "3" and role == "admin":
                    ubah_produk()
                    back()
                    clear()

                elif pilih == "4":
                    if role == "admin":
                        hapus_produk()
                    else:
                        beli_produk(username)
                    back()
                    clear()

                elif pilih == "5":
                    tampilkan_total_harga()
                    back()
                    clear()

                elif pilih == "6" and role == "admin":
                    tampilkan_data_user()
                    back()
                    clear()

                elif pilih == "7":
                    print("Terima Kasih Telah Melihat Produk Kami")
                    loading(3)
                    clear()
                    break

                else:
                    print("Pilihan Tidak Valid!")

    # Register Hanya Untuk Pengunjung
    elif pilihan == "2":
        user_register()
        back()

    # Keluar
    elif pilihan == "3":
        print("Terima Kasih Telah Berkunjung.")
        break

    else:
        print("Pilihan Tidak Valid!")
