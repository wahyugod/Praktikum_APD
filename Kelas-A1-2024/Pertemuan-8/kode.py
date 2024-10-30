# x = 0
# assert x!= 0

# x = 12
# x.append(10)

# import os
# os.system("PAUSE")

# dict = {
#     "key" : 1
# }

# print(dict["lele"])

# print(x)

# num=11
# print("hello"+num)

# if num == 10:
# print(num)

# try:
#     angka = int(input("Masukkan angka: "))
#     print(angka)
# except ValueError:
#     print("input salah")
# else:
#     print("berhasil")
# finally:
#     print("wahyu")

# x = 1
# y = 0
# print(x/y)

# try:
#     nama = str(input("nama kamu: "))
#     if len(nama) > 5:
#         raise ValueError ("nama tidak boleh lebih dari")
# except ValueError as e:
#     print(e)

# try:
#     nim = input("masukan nim anda: ")
#     if not nim:
#         raise ValueError("nim tidak boleh kosong")
#     if not nim.isdigit():
#         raise TypeError("nim harus angka")
#     if len(nim)!=10:
#         raise ValueError("nim harus 10 digit")
# except TypeError as T:
#     print(T)
# except ValueError as e:
#     print(e)
# else:
#     print(f"nim anda adalah {nim}")
# finally:
#     print("selesai")

# path = "./folder_ini/data.txt"
# file = open(path, "w")

# with open(path, "r") as file:
#     konten = file.read()
#     print(konten)
#     for i in file:
#         print(i, end=" ")

# with open(path,"w") as file:
#     file.write("ambatukam,28,waria\n")
#     file.write("rusdi,69,pria?")

# with open(path, "r") as file:
#     konten = file.read()
#     print(konten)

# try:
#     with open("data.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File tidak ditemukan")

path = "./folder_ini/faiz.csv"
with open(path, "w") as file:
    file.write("lele")