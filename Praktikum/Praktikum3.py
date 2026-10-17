#Seorang mahasiswa memenuhi syarat kelulusan praktikum jika nilai minimal 75 dan kehadiran minimal 80%. 
#Gunakan data awal nilai = 82 dan kehadiran = 90. 
#Tugas: 
#1. Buat variabel nilai dan kehadiran.
nilai = 82
kehadiran = 90 
#2. Gunakan operator >= untuk memeriksa masing-masing syarat.
nilai >= 75
kehadiran >= 100*80/100
#3. Gunakan operator and untuk menentukan apakah mahasiswa memenuhi kedua syarat.
syarat = nilai >= 75 and kehadiran >= 100*80/100
print(syarat)
#4. Ubah nilai menjadi 70.
nilai = 70
#Jalankan kembali program dan amati perubahan hasil. 
#5. Coba gunakan or. Jelaskan perbedaan hasilnya.
nilai >= 75 or kehadiran >= 100*80/100
#Gada bedanya sama sama satu hasilnya perbedaannya terletak di cara ukur truenya yang satu dua duanya harus true
#yang satu lagi cukup salah satunya true
print(syarat)

