import csv
from tabulate import tabulate
import os
import time
import sys

#Warna
BOLD = '\033[1m'
RED = '\033[31m'
GREEN = '\033[32m'
MAGENTA = '\033[35m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
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

def animasi_output(teks, delay=0.5):
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
        tabel_data = [[no, data["nama"], data['merek'], data['prosesor'], data['vga'], f"Rp{data['harga']}"]
                      for no, data in produk_laptop.items()]
        print(tabulate(tabel_data, headers=["No", "Nama", "Merek", "Prosesor", "VGA", "Harga"], tablefmt="grid"))

# Prosedur Untuk Menambah Produk
def tambah_produk():
    nama_produk = input(BOLD + "\nMasukan Nama Laptop Yang Ingin Ditambah: " + RESET)
    if not nama_produk.strip():
        print(RED + "Input Tidak Boleh Kosong" + RESET)
        return
    nama_produk = nama_produk.upper()

    for produk in produk_laptop.values():
        if produk["nama"] == nama_produk:
            print(RED + f"Produk Dengan Nama '{nama_produk}' Sudah Ada!" + RESET)
            return

    merek = input(BOLD + "Masukan Merek Laptop : " + RESET)
    if not merek.strip():
        print(RED + "Input Tidak Boleh Kosong" + RESET)
        return

    prosesor = input(BOLD + "Masukan Prosesor Laptop : " + RESET)
    if not prosesor.strip():
        print(RED + "Input Tidak Boleh Kosong" + RESET)
        return

    vga = input(BOLD + "Masukan VGA Laptop : " + RESET)
    if not vga.strip():
        print(RED + "Input Tidak Boleh Kosong" + RESET)
        return

    try:
        harga = int(input(BOLD + "Masukan Harga : " + RESET))
        if harga <= 0:
            print(RED + "Harga Tidak Boleh Minus atau 0" + RESET)
            return
    except ValueError:
        print(RED + "Harga Harus Berupa Angka!" + RESET)
        return

    # Tambahkan produk ke dictionary
    produk_laptop[len(produk_laptop) + 1] = {
        "nama": nama_produk,
        "merek": merek,
        "prosesor": prosesor,
        "vga": vga,
        "harga": harga,
    }
    simpan_data_csv()
    print(GREEN + f"Produk '{nama_produk}' Berhasil Ditambahkan!" + RESET)


# Prosedur Untuk Mengubah Produk
def ubah_produk():
    tampilkan_produk()
    try:
        nomor = int(input(BOLD+"Masukkan Nomor Produk yang ingin diubah: "+RESET))
        if nomor in produk_laptop:
            produk = produk_laptop[nomor]
            nama_baru = input(BOLD+"Masukan Nama Baru : "+RESET) or produk["nama"]

            for produk in produk_laptop.values():
                if produk["nama"] == nama_baru.upper():
                    print(RED + f"Produk Dengan Nama '{nama_baru}' Sudah Ada!" + RESET)
                    return
            
            if not nama_baru.strip():
                print(RED+ 'Input Tidak Boleh Kosong'+RESET)
                return

            merek_baru = input(BOLD+"Masukan Merek Baru : "+RESET) or produk["merek"]
            if not merek_baru.strip():
                print(RED+ 'Input Tidak Boleh Kosong'+RESET)
                return
            prosesor_baru = input(BOLD+"Masukan Prosesor Baru : "+RESET) or produk["prosesor"]
            if not prosesor_baru.strip():
                print(RED+ 'Input Tidak Boleh Kosong'+RESET)
                return
            vga_baru = input(BOLD+"Masukan VGA Baru : "+RESET) or produk["vga"]
            if not vga_baru.strip():
                print(RED+ 'Input Tidak Boleh Kosong'+RESET)
                return
            harga_baru = int(input(BOLD+"Masukan Harga Baru : "+RESET) or produk["harga"])
            if harga_baru <= 0:
                print(RED + "Harga Tidak Boleh Minus atau 0" + RESET)
                return
            produk_laptop[nomor] = {
                "nama": nama_baru,
                "merek": merek_baru,
                "prosesor": prosesor_baru,
                "vga": vga_baru,
                "harga": harga_baru
            }
            simpan_data_csv()
            print("Produk Berhasil Diubah!")
        else:
            print(RED+"Nomor Tidak Ditemukan!"+RESET)
    except ValueError:
        print(RED+"Input Harus Berupa Angka!"+RESET)

# Prosedur Hapus Produk
def hapus_produk():
    tampilkan_produk()
    try:
        nomor = int(input(BOLD+"Masukkan Nomor Produk yang ingin dihapus: "+RESET))
        if nomor in produk_laptop:
            del produk_laptop[nomor]
            rapikan_nomor_produk()
            simpan_data_csv()
            print(f"Produk dengan nomor {nomor} berhasil dihapus.")
        else:
            print(RED+"Nomor Tidak Ditemukan!"+RESET)
    except ValueError:
        print(RED+"Input Harus Berupa Angka!"+RESET)

def beli_produk(username):
    tampilkan_produk()
    try:
        nomor = int(input(BOLD+"Masukkan Nomor Produk yang ingin dibeli: "+RESET))
        if nomor in produk_laptop:
            produk = produk_laptop.pop(nomor)
            produk_dibeli.append(produk)
            user[username]["produk_dibeli"].append(produk["nama"])
            rapikan_nomor_produk()
            simpan_data_csv()
            print(f"Produk '{produk['nama']}' berhasil dibeli.")
        else:
            print(RED+"Nomor Tidak Ditemukan!"+RESET)
    except ValueError:
        print(RED+"Input Harus Berupa Angka!"+RESET)

# Fungsi Total Harga
def tampilkan_total_harga():
    total = hitung_total_harga()
    print(f"\nTotal Harga Semua Produk: Rp{total}")

# Fungsi Total Harga untuk Produk yang Dibeli Pengunjung
def tampilkan_total_harga_pengunjung(username):
    if not user[username]["produk_dibeli"]:
        print("Anda belum membeli produk apa pun.")
        return

    total_harga = 0
    for produk in produk_dibeli:
        if produk["nama"] in user[username]["produk_dibeli"]:
            total_harga += produk["harga"]
    print(f"\nTotal Harga Produk yang Anda Beli: Rp{total_harga}")

def rapikan_nomor_produk():
    produk_laptop_urut = {i+1: data for i, data in enumerate(produk_laptop.values())}
    produk_laptop.clear()
    produk_laptop.update(produk_laptop_urut)

# Fungsi Simpan Data ke CSV
def simpan_data_csv():
    with open('data_produk.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Merek", "Prosesor", "VGA", "Harga"])
        for data in produk_laptop.values():
            writer.writerow([data["nama"], data["merek"], data["prosesor"], data["vga"], data["harga"]])

# Fungsi Muat Data dari CSV
def muat_data_csv():
    try:
        with open('data_produk.csv', 'r') as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader, start=1):
                produk_laptop[i] = {
                    "nama": row["Nama"],
                    "merek": row["Merek"],
                    "prosesor": row["Prosesor"],
                    "vga": row["VGA"],
                    "harga": int(row["Harga"])
                }
    except FileNotFoundError:
        print(RED+"File data_produk.csv tidak ditemukan"+RESET)

def user_register():
    username_baru = input(BOLD+"\nMasukkan Username Baru : "+RESET)
    if not username_baru.strip():
        print(RED+"Input Tidak Boleh Kosong"+RESET)
    else:
        password_baru = input(BOLD+"Masukkan Password Baru : "+RESET)
        if not password_baru.strip():
            print(RED+"Input Tidak Boleh Kosong"+RESET)
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
    if len(data_pengunjung) == 0:
        print("Tidak ada pengunjung yang terdaftar.")
    else:
        print("\nBerikut Adalah Data Pengunjung")
        tabel_data = []
        for username, data in user.items():
            if data["role"] == "pengunjung":
                produk_dibeli = ", ".join(data["produk_dibeli"]) if data["produk_dibeli"] else "Tidak ada"
                tabel_data.append([username, data['password'], produk_dibeli])
        
        animasi_output(tabulate(tabel_data, headers=["Username", "Password", "Produk Dibeli"], tablefmt="grid"), delay=0.01)

def login_menu():
    animasi_output(GREEN+"\n=================================", delay=0.01)
    animasi_output("|    Toko Laptop Wahyu Jaya     |", delay=0.01)
    animasi_output("=================================", delay= 0.01)
    animasi_output("| 1. Login                      |", delay= 0.01)
    animasi_output("| 2. Register                   |", delay= 0.01)
    animasi_output("| 3. Keluar                     |", delay= 0.01)
    animasi_output("================================="+RESET, delay=0.01)

def main_menu():
    if role == "admin":
        animasi_output(MAGENTA+"\n=================================", delay=0.01)
        animasi_output("|    Toko Laptop Wahyu Jaya     |", delay=0.01)
        animasi_output("=================================", delay=0.01)
        animasi_output("| 1. Tampilkan Produk           |", delay=0.01)
        animasi_output("| 2. Tambah Produk              |", delay=0.01)
        animasi_output("| 3. Ubah Produk                |", delay=0.01)
        animasi_output("| 4. Hapus Produk               |", delay=0.01)
        animasi_output("| 5. Tampilkan Total Harga      |", delay=0.01)
        animasi_output("| 6. Tampilkan Data User        |", delay=0.01)
        animasi_output("| 7. Keluar                     |", delay=0.01)
        animasi_output("================================="+RESET, delay=0.01)
    else:
        animasi_output(BRIGHT_YELLOW+"\n=================================", delay=0.01)
        animasi_output("|    Toko Laptop Wahyu Jaya     |", delay=0.01)
        animasi_output("=================================", delay=0.01)
        animasi_output("| 1. Tampilkan Produk           |", delay=0.01)
        animasi_output("| 2. Beli Produk                |", delay=0.01)
        animasi_output("| 3. Tampilkan Total Harga      |", delay=0.01)
        animasi_output("| 4. Keluar                     |", delay=0.01)
        animasi_output("================================="+RESET, delay=0.01)

def back():
    input("Tekan Enter Untuk Melanjutkan...")

# Sesi Login
muat_data_csv()
while True:
    clear()
    login_menu()
    pilihan = input(BOLD+"Masukan Pilihan : "+RESET)
    clear()

    if pilihan == "1":
        username = input("\nMasukkan Username : ")
        password = input("Masukkan Password : ")
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
                    tampilkan_produk()
                    tambah_produk()
                    back()
                    loading(2)
                    clear()
                
                elif pilih == "2" and role == "pengunjung":
                    beli_produk(username)
                    back()
                    loading(2)
                    clear()

                elif pilih == "3" and role == "admin":
                    ubah_produk()
                    back()
                    loading(2)
                    clear()
                
                elif pilih == "3" and role == "pengunjung":
                    tampilkan_total_harga_pengunjung(username)
                    back()
                    loading(2)
                    clear()

                elif pilih == "4"and role == "admin":
                    hapus_produk()
                    back()
                    loading(2)
                    clear()

                elif pilih == "4" and role == "pengunjung":
                    print("Terima Kasih Telah Melihat Produk Kami")
                    loading(2)
                    clear()
                    break

                elif pilih == "5" and role == "admin":
                    tampilkan_total_harga()
                    back()
                    loading(2)
                    clear()

                elif pilih == "6" and role == "admin":
                    tampilkan_data_user()
                    back()
                    loading(2)
                    clear()

                elif pilih == "7" and role == "admin":
                    print("Terima Kasih Telah Melihat Produk Kami")
                    loading(2)
                    clear()
                    break

                else:
                    print("Pilihan Tidak Valid!")
                    loading(1)
                    clear()

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
        clear()