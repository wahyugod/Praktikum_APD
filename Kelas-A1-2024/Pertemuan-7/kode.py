# def salam():
#     print("woi cepattt, taktis")
# salam()

# def kali():
#     x = 6*4
#     print(x)

# kali()

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("Luas persegi panjang:", luas)

# luas_persegi_panjang(4, 6)

# sisi = 2
# luas = sisi * sisi

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# print ("Luas persegi :", luas_persegi(8))
# print(luas)

# luas = luas_persegi(5)
# print(luas)

# membuat variabel global
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# # membuat variabel lokal
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"
# # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)

# def info2():
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)

# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# # memanggil fungsi info
# info()
# info2()

# buku = []
# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])

# def insert_data():
#     buku_baru = input("Judul Buku : ")
#     buku.append(buku_baru)

# def edit_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         judul_baru = input("Judul baru: ")
#         buku[indeks] = judul_baru

# def delete_data():
#     show_data()
#     indeks = int(input("Inputkan ID buku: "))
#     if(indeks >= len(buku) or indeks < 0):
#         print ("ID salah")
#     else:
#         buku.remove(buku[indeks])

# def show_menu():
#     print ("\n")
#     print ("----------- MENU---------- ")
#     print ("[1] Show Data")
#     print ("[2] Insert Data")
#     print ("[3] Edit Data")
#     print ("[4] Delete Data")
#     print ("[5] Exit")
#     menu = input("PILIH MENU> ")
#     print ("\n")
#     if menu == "1":
#         show_data()
#     elif menu == "2":
#         insert_data()
#     elif menu == "3":
#         edit_data()
#     elif menu == "4":
#         delete_data()
#     elif menu == "5":
#         exit()
#     else:
#         print ("Salah pilih!")

# while(True):
#     show_menu()

# def square_root(num):
#     precision=0.00001
#     if num < o:
#         return "angka negatif tidak memiliki akar yang terdefinisi"
#     guess = num / 2.0
#     while abs(guess * guess - num ):

# import math
# import pandas
# angka = 49
# print(math.sqrt(angka))

# def luas_segitiga():
#     alas = int(input("masukan alas : "))
#     tinggi = int(input("masukan tinggi : "))
#     luas = 0.5 * alas * tinggi
#     print(luas)

# def luas_persegi_panjang():
#     panjang = int(input("masukan panjang : "))
#     lebar = int(input("masukan lebar : "))
#     luas = panjang * lebar
#     print(luas)

# luas_segitiga()
# luas_persegi_panjang()