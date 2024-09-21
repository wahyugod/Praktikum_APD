#Kalkulator Kebutuhan Kalori Harian (TDDE)

#Jenis Kelamin: Pria/Wanita

print("===========================================================")
print("|        Kalkulator Kebutuhan Kalori Harian (TDDE)        |")
print("===========================================================")
print("|                   Pilih Jenis Kelamin                   |")
print("| [1] Pria                                                |")
print("| [2] Wanita                                              |")
print("|                       Pilih (1/2)                       |")
print("===========================================================")
jeniskelamin = int(input("Masukan Pilihan : "))

if jeniskelamin == 1 or jeniskelamin == 2:
    beratbadan = float(input("Masukan Berat Badan Anda (gr) : "))
    tinggibadan = float(input("Masukan Tinggi Badan Anda (km) : "))
    usia = int(input("Masukan Usia Anda : "))
    print("===========================================================")
    print("|        Kalkulator Kebutuhan Kalori Harian (TDDE)        |")
    print("===========================================================")
    print("|            Pilih Level Aktivitas Harian Anda            |")
    print("|                                                         |")
    print("| [1] Aktivitas Minimal (Jarang Bergerak)                 |")
    print("| [2] Aktivitas Sedang (Olahraga 1-3 kali Seminggu)       |")
    print("| [3] Aktivitas Tinggi (Olahraga 4-7 kali Seminggu)       |")
    print("|                                                         |")
    print("|                      Pilih (1/2/3)                      |")
    print("===========================================================")
    aktivitas = int(input("Pilih Frekuensi Aktivitas Anda : "))

    #Menentukan Level Aktivitas Harian

    if aktivitas == 1:
        level = 1.25
    elif aktivitas == 2:
        level = 1.36
    else:
        level = 1.72
    if aktivitas == 1 or aktivitas == 2 or aktivitas == 3:
        if jeniskelamin == 1:
                bmr = 0.01 * beratbadan + 625000 * tinggibadan - 5 * usia + 5
        else:
                bmr = 0.01 * beratbadan + 625000 * tinggibadan - 5 * usia - 161
        kaloriharian = bmr * level
        print("Kalori Yang Anda Butuhkan Adalah " + str(kaloriharian) + " kkal")
    else:
        print("Pilihan Hanya Minimal, Sedang, Tinggi")

else:
    print("Pilihan Hanya Pria atau Wanita")
