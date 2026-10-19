#Buat program untuk mengelola data sederhana berikut. 
# nilai = [78, 85, 90, 85]
nilai = [78, 85, 90, 85]
# mahasiswa = {"nama": "Nadia", "kelas": "IF-A"}
mahasiswa = {"nama": "Nadia", "kelas": "IF-A"} 
# koordinat = (5, 8) 
koordinat = (5, 8)
# angka = {2, 4, 4, 6, 8}
angka = {2, 4, 4, 6, 8} 
#Tugas: 
#1. Tampilkan nilai pertama dari list.
print(nilai[0]) 
#2. Tambahkan nilai 95 ke list dan tampilkan list terbaru.
nilai.append(95)
print(nilai)
#3. Tampilkan nama mahasiswa dari dictionary. 
print(mahasiswa)
#4. Tampilkan koordinat pertama dari tuple.
print(koordinat[0])
#5. Tampilkan angka unik dengan sorted(angka).
print(sorted(angka)) 
#6. Jelaskan mengapa angka 4 hanya muncul satu kali pada set. Karena itulah hidup secukupnya aja jangan banyak banyak
#karena udah di sorted jadi dengan shorted hanya akan menampilkan angka unik dan tidak duplikat