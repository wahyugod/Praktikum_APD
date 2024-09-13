namalengkap = input("Masukan Nama Lengkap : ")
namapanggilan = input("Masukan Nama Panggilan : ")
nim = int(input("Masukan NIM : "))

namauniversitas = input()
namafakultas = input()
namaprodi = input()
umur = int(input())

# tinggibadan dalam meter
tinggibadan = float(input())
beratbadan = int(input())
b = beratbadan * 2.205
a = 10 % 6

print("Nama saya " + namalengkap + " ,biasa dipanggil " + namapanggilan + " dengan NIM " + nim + ". Saya kuliah di Universitas " + namauniversitas + " Fakultas " + namafakultas + " Prodi " + namaprodi + ". Tinggi saya " + tinggibadan + "m dan berat " + beratbadan + "kg atau " + b + " lbs")