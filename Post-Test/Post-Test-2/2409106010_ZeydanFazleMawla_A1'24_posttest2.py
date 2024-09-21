namalengkap = input("Masukan Nama Lengkap : ")
namapanggilan = input("Masukan Nama Panggilan : ")
nim = int(input("Masukan NIM : "))
namaprodi = input("Masukan Nama Prodi : ")
umur = int(input("Masukan Umur : "))

tinggibadan = float(input("Masukan Tinggi Badan (m) : "))
beratbadan = float(input("Masukan Berat Badan (kg) : "))

konversilbs = beratbadan * 2.205
modnim = 10 % 6

print("Nama saya " + namalengkap + ", biasa dipanggil " + namapanggilan + " dengan NIM " + str(nim) + " Prodi " + namaprodi + ". Saya berumur " + str(umur) + " tahun," " tinggi saya " + str(tinggibadan) + " m dan berat " + str(beratbadan) + " kg atau " + str(konversilbs) + " lbs. " + str(modnim))