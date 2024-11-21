import csv
from tabulate import tabulate
import os
import time
import sys

#Warna
BOLD = '\033[1m'
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m' 
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
LIGHT_GRAY = '\033[37m'
DARK_GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m' 

# CRUD Manajemen Produk Laptop

user = {
    "admin": {"password": "admin", "role": "admin"}
}
produk_laptop = {}
data_pengunjung = []
produk_dibeli = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def animasi_output(teks, delay=0.0000001):
    for huruf in teks:
       sys.stdout.write(huruf)
       sys.stdout.flush()
       time.sleep(delay)
    print()
    
def loading(duration=5):
    animation = [
        BRIGHT_BLUE+"Loading .   ",
        "Loading ..  ",
        "Loading ... ",
        "Loading     "+RESET
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
        tabel_data = [[nama, data['merek'], data['prosesor'], data['vga'], f"Rp{data['harga']}"] 
        for nama, data in produk_laptop.items()]
        animasi_output(tabulate(tabel_data, headers=["Nama", "Merek", "Prosesor", "VGA", "Harga"], tablefmt="grid"), delay=0.0000001)
        
# Prosedur Untuk Menambah Produk
def tambah_produk():
    nama_produk = input(BOLD+"Masukan Nama Laptop : "+RESET)
    if not nama_produk.strip():
        print('Input tidak boleh kosong')
        return
    else:
        pass
    if nama_produk in produk_laptop:
        print(f"Produk Dengan Nama '{nama_produk}' Sudah Ada!")
        return

    merek = input(BOLD+"Masukan Merek Laptop : "+RESET)
    if not merek.strip():
        print('Input tidak boleh kosong')
        return
    else:
        pass
    prosesor = input(BOLD+"Masukan Prosesor Laptop : "+RESET)
    if not prosesor.strip():
        print('Input tidak boleh kosong')
        return
    else:
        pass
    vga = input(BOLD+"Masukan VGA Laptop : "+RESET)
    if not vga.strip():
        print('Input tidak boleh kosong')
        return
    else:
        pass

    while True:
        try:
            harga = int(input(BOLD+"Masukan Harga : "+RESET))
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
    nama_lama = input(BOLD+"Masukan Nama Produk yang ingin diubah: "+RESET)

    if nama_lama in produk_laptop:
        try:
            nama_baru = input(BOLD+"Masukan Nama Baru : "+RESET)
            if not nama_baru.strip():
                print('Input tidak boleh kosong')
                return
            else:
                pass
            merek_baru = input(BOLD+"Masukan Merek Baru : "+RESET)
            if not merek_baru.strip():
                print('Input tidak boleh kosong')
                return
            else:
                pass
            prosesor_baru = input(BOLD+"Masukan Prosesor Baru : "+RESET)
            if not prosesor_baru.strip():
                print('Input tidak boleh kosong')
                return
            else:
                pass
            vga_baru = input(BOLD+"Masukan VGA Baru : "+RESET)
            if not vga_baru.strip():
                print('Input tidak boleh kosong')
                return
            else:
                pass
            harga_baru = int(input(BOLD+"Masukan Harga Baru : "+RESET))

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
        nama_lama = input(BOLD+"Masukan Nama Yang Ingin Dihapus : "+RESET)
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
        nama_produk = input(BOLD+"Masukkan nama produk yang ingin dibeli: "+RESET)
        if nama_produk in produk_laptop:
            produk_dibeli.append(produk_laptop[nama_produk]) 
            user[username]["produk_dibeli"].append(nama_produk) 
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
    username_baru = input(BOLD+"Masukkan Username Baru : "+RESET)
    if not username_baru.strip():
        print('Input tidak boleh kosong')
    else:
        password_baru = input(BOLD+"Masukkan Password Baru : "+RESET)
        if not password_baru.strip():
            print('Input tidak boleh kosong')
        else:
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
        
        animasi_output(tabulate(tabel_data, headers=["Username", "Password", "Produk Dibeli"], tablefmt="grid"), delay=0.0000001)

def login_menu():
    animasi_output(GREEN+"\n=================================", delay=0.0000001)
    animasi_output("|    Toko Laptop Wahyu Jaya     |", delay=0.0000001)
    animasi_output("=================================", delay= 0.0000001)
    animasi_output("| 1. Login                      |", delay= 0.0000001)
    animasi_output("| 2. Register                   |", delay= 0.0000001)
    animasi_output("| 3. Keluar                     |", delay= 0.0000001)
    animasi_output("================================="+RESET, delay=0.0000001)

def main_menu():
    if role == "admin":
        print(MAGENTA+"\n=================================")
        print("|    Toko Laptop Wahyu Jaya     |")
        print("=================================")
        print("| 1. Tampilkan Produk           |")
        print("| 2. Tambah Produk              |")
        print("| 3. Ubah Produk                |")
        print("| 4. Hapus Produk               |")
        print("| 5. Tampilkan Total Harga      |")
        print("| 6. Tampilkan Data User        |")
        print("| 7. Keluar                     |")
        print("================================="+RESET)
    else:
        print(BRIGHT_YELLOW+"\n=================================")
        print("|    Toko Laptop Wahyu Jaya     |")
        print("=================================")
        print("| 1. Tampilkan Produk           |")
        print("| 4. Beli Produk                |")
        print("| 5. Tampilkan Total Harga      |")
        print("| 7. Keluar                     |")
        print("================================="+RESET)

def back():
    input("Tekan Enter Untuk Melanjutkan...")

# Sesi Login
muat_data_csv()
while True:
    clear()
    loading(1)
    clear()
    login_menu()
    pilihan = input(BOLD+"Masukan Pilihan : "+RESET)
    clear()

    if pilihan == "1":
        username = input(BOLD+"\nMasukkan Username : "+RESET)
        password = input(BOLD+"Masukkan Password : "+RESET)
        role = login(username, password)
        back()
        loading(1)
        clear()

        # Program Utama CRUD
        if role:
            while True:
                main_menu()
                pilih = input(BOLD+"Masukan Pilihan : "+RESET)
                loading(1)
                clear()

                if pilih == "1":
                    tampilkan_produk()
                    back()
                    loading(2)
                    clear()

                elif pilih == "2" and role == "admin":
                    tambah_produk()
                    back()
                    loading(2)
                    clear()

                elif pilih == "3" and role == "admin":
                    ubah_produk()
                    back()
                    loading(2)
                    clear()

                elif pilih == "4":
                    if role == "admin":
                        hapus_produk()
                    else:
                        beli_produk(username)
                    back()
                    loading(2)
                    clear()

                elif pilih == "5":
                    tampilkan_total_harga()
                    back()
                    loading(2)
                    clear()

                elif pilih == "6" and role == "admin":
                    tampilkan_data_user()
                    back()
                    loading(2)
                    clear()

                elif pilih == "7":
                    print("Terima Kasih Telah Melihat Produk Kami")
                    loading(2)
                    clear()
                    break

                else:
                    print("Pilihan Tidak Valid!")

    # Register Hanya Untuk Pengunjung
    elif pilihan == "2":
        user_register()
        back()
        loading(2)

    # Keluar
    elif pilihan == "3":
        print("Terima Kasih Telah Berkunjung.")
        loading(2)
        clear()
        break

    else:
        print("Pilihan Tidak Valid!")
        loading(1)
