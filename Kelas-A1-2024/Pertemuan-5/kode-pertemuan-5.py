# nama = ["wahyu", "kingfaiz", "riyadi", "farel", "celio", "vito", "jaka", "adon", "yusri", "aan"]
# matkul = ["APD", "APL", "WEB", "Kalkulus"]
# data = nama+matkul

# print("sebelum :")
# print(nama)
# print("")
# print("sesudah :")
# print("")

# print(type(nama))
# print(nama[0])
# print(nama[2:5])

# nama.append("zakaria")
# print(nama)
# nama.insert(2,"wahyugod")
# print(nama)

# nama[0]= "wahyugod"
# print(nama)

# del nama[2]
# print(nama)

# hapus = nama.pop(2)
# print(nama)
# print(hapus)

# print(nama[2:4])
# print(nama[1:10:2])

# print(nama+matkul)
# print(matkul*3)
# print(data*3)

# tes = [["wahyu", "kingfaiz"], [1, 2,"halo",True, False, "alufeed", "zilong", "gatotkaca"]]

# print(tes)
# print(tes[2][3][-1])
# print(tes[-1])

# for i in nama:
#     print(i, end=" ")
#     print("")

# for i in tes:
#     for j in i:
#         print(j)

# nama1 = ("wahyu", "kingfaiz", "riyadi", "farel", "celio", "vito", "jaka", "adon", "yusri", "aan")
# print(nama1)

# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")

# absen, prodi, nim, nama = mahasiswa

# print(absen)
# print(prodi)
# print(nim)
# print(nama)

# print(
# """
# ================
#  DATA MAHASISWA
# ================
# 1. Tambah Data
# 2. Tampilan Data
# 3. Ubah Data
# 4. Hapus Data
# 5. Keluar
# ===============
# """
# )
# data_mahasiswa = []
# while True:
#     pilih=int(input("pilih : "))
#     if pilih == 1:
#         nama=input("nama : ")
#         nim=input("nim : ")
#         kelas=("kelas : ")
#         data_mahasiswa.append([nama,nim,kelas])
#     elif pilih==2:
#         for i in data_mahasiswa:
#             for i in range(len(data)):
#                 print(f"\n Data Mahasiswa ke-{i+1}")
#     elif pilih==5:
#         print("terima kasih")

#CRUD
# print( 
# """
# ===========================
# |   DATA MAHASISWA A24    |
# ===========================
# |    1. TAMBAH DATA       |           
# |    2. TAMPILKAN DATA    |          
# |    3. UBAH DATA         |     
# |    4. HAPUS DATA        |      
# |    5. KELUAR            |  
# ===========================
# """
# )

# data_mahasiswa = []
# while True:
#     pilih = int(input("PILIH : "))
#     if pilih == 1:
#         nama = input("NAMA : ")
#         nim = input("NIM : ")
#         kelas = input("KELAS : ")
#         data_mahasiswa.append([nama,nim,kelas])
#     elif pilih == 2:
#         for i in range(len(data_mahasiswa)):
#             print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
#     elif pilih == 3:
#         nama_lama = input("Nama Baru : ")
#         for i in range(len(data_mahasiswa)):
#             if data_mahasiswa[i][0] == nama_lama:
#                 nama_baru = input("NAMA : ")
#                 nim_baru = input("NIM : ")
#                 kelas_baru = input("KELAS : ")
#                 data_mahasiswa[i][0] = nama_baru
#                 data_mahasiswa[i][1] = nim_baru
#                 data_mahasiswa[i][2] = kelas_baru
#     elif pilih == 4:
#         nama_lama = input("Nama yang ingin dihapus")
#         for i in range(len(data_mahasiswa)):
#             if data_mahasiswa[i][0] == nama_lama:
#                 del data_mahasiswa[i]
#     elif pilih == 5:
#         print("Terima Kasih Telah Mengakses Data Mahasiswa")
#         break
#     else:
#         print("Anda Salah Input")

























