# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku1" : "Percy Jackson",
# "Buku3" : "Twillight"
# }

# # print(daftar_buku["Buku1"])
# # print(daftar_buku["Buku2"])
# # print(daftar_buku["Buku3"])

# print(daftar_buku["Buku1"])

# daftar_buku = {}
# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"
# print(daftar_buku)

# games = dict(sekiro = "action", pokemon = "adventure", valorant = "fps")
# print(games)

# print(Biodata["KRS"][1])
# print(Biodata.get("Lele"))
# print(Biodata.get("Lele", "Nyari Apa Lek"))

# for i in Biodata.items():
#     print(i)

# for i, j in Biodata.items():
#     print(f"Key = {i} dan value = {j}" )

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

# print("Film : ", Film.setdefault("Oldbook", "Horror"))
# print(Film)

# for i in Film.keys():
#     print(i, end=" ")

# for i in Film.values():
#     print(i, end=" ")

# print(Film)
# print(Film)
# Film["Zombie Land"] = "Comedy"
# Film.update({"Hour" : "Thriller"})

# del Film["The Conjuring"]
# hapus = Film.pop("The Conjuring")
# print(Film)
# print(f"Key yang dihapus {hapus}")
# Film.clear()
# print(Film)

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# print("Jumlah data dalam dict Biodata", len(Biodata))
# pinjamdict = Biodata.copy()
# print(pinjamdict)

# key = "Apel", "Jeruk", "Mangga"
# value = 1

# buah = dict.fromkeys(key, value)
# print(buah)

# Musik = {
#     "The Chainsmoker" : ["All we Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for lagu in j:
#         print(lagu)
#     print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# print(mahasiswa)
# mahasiswa[101]["Angkatan"] = 2023
# del mahasiswa[111]["Umur"]
# print(mahasiswa)

# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#     print("")

# Membuat dictionary dengan data mata pelajaran dan nilai


# nilai_pelajaran = {
#     "Matematika": 90,
#     "Fisika": 80,
#     "Biologi": 80,
#     "Kimia": 70
# }

# total_nilai = sum(nilai_pelajaran.values())
# rata_rata_nilai = total_nilai / len(nilai_pelajaran)
# print(f"totalnya adalah {total_nilai} dan rata ratanya adalah {rata_rata_nilai}")

# anu = {
#     "nama" : "wahyu",
#     "nim" : "2409106031",
#     "umur" : "18",
#     "jurusan" : "sastra mesin",
#     "angkatan" : "2099"
# }

# print(anu.get("nim"))


Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")