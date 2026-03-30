# ==========================================
# 1. Deklarasi Variabel dan Tipe Data
# ==========================================
nama_ku = "CINDI"      
semester = 6               
ipk_target = 4.00          
suka_ngoding = True           
belajar = ["python", "ai", "C", "C++", "Java"] 

# ==========================================
# 2. Manipulasi String
# ==========================================
print("--- Manipulasi String ---")
pesan = "Semangat belajar Cin!"

print("Pesan Asli: " + pesan)
print("Gabungan: Aku " + nama_ku + " adalah Mahasiswa Teknik Infromatika.")
print("Panjang karakter pesan:", len(pesan))
print("Huruf Besar:", pesan.upper())
print("Huruf Kecil:", pesan.lower())
print("\n") 

# ==========================================
# 3. Operasi Matematika Sederhana
# ==========================================
print("--- Operasi Matematika ---")
angka1 = 15
angka2 = 4

print("Penjumlahan (15 + 4)  =", angka1 + angka2)
print("Pengurangan (15 - 4)  =", angka1 - angka2)
print("Perkalian   (15 * 4)  =", angka1 * angka2)
print("Pembagian   (15 / 4)  =", angka1 / angka2)
print("Bagi Bulat  (15 // 4) =", angka1 // angka2)
print("Sisa Bagi   (15 % 4)  =", angka1 % angka2)
print("\n")

# ==========================================
# 4. List dan Akses Elemen
# ==========================================
print("--- Manipulasi List ---")
print("List awal:", belajar)
print("Elemen ke-3:", belajar[2])

belajar.append("OpenGL")
print("Setelah ditambah item baru:", belajar)

belajar.remove("C++")
print("Setelah item C++ dihapus:", belajar)
print("\n")

# ==========================================
# 5. Penggunaan Input dari User
# ==========================================
print("--- Perkenalan Diri ---")
nama_user = input("Masukkan nama kamu: ")
umur_user = input("Masukkan umur kamu: ")

print("Halo, nama saya " + nama_user + " dan umur saya " + umur_user + " tahun.")