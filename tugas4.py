# ==========================================
# 1. LIST - Akses & Manipulasi
# ==========================================
print("--- 1. LIST ---")
# List dengan 6 elemen campuran
data_campuran = ["KERIS", 2026, 3.95, True, "UISU", "Informatika"]

print("List Awal:", data_campuran)
print("Elemen Pertama:", data_campuran[0])
print("Elemen Terakhir:", data_campuran[-1])
print("Slicing [1:5:2]:", data_campuran[1:5:2]) # Ambil dari indeks 1 sampai 4, lompat 2

# Manipulasi List
print("\nSebelum dimanipulasi:", data_campuran)
data_campuran.append("AI")              # Tambah di akhir
data_campuran.insert(2, "HIMATIF")      # Sisipkan di indeks 2
data_campuran.extend(["React", "Node"]) # Tambah banyak elemen
data_campuran.pop()                     # Hapus elemen paling akhir (Node)
data_campuran.remove(True)              # Hapus elemen yang bernilai True
print("Sesudah dimanipulasi:", data_campuran)
print("\n")

# ==========================================
# 2. TUPLE - Immutability & Unpacking
# ==========================================
print("--- 2. TUPLE ---")
# Tuple tidak bisa diubah isinya (immutable)
info_tuple = ("Cindi", 6, "Teknik Informatika", "Basudara", "Medan")

print("Isi Tuple:", info_tuple)
print("Panjang Tuple:", len(info_tuple))
print("Akses Indeks ke-2:", info_tuple[2])

# Unpacking dengan *rest
nama, semester, *info_lain = info_tuple
print(f"Unpacking -> Nama: {nama}, Semester: {semester}, Info Lainnya: {info_lain}")
print("\n")

# ==========================================
# 3. SET - Keunikan & Operasi Himpunan
# ==========================================
print("--- 3. SET ---")
# Set otomatis membuang data yang dobel/duplikat
set_a = {"Python", "React", "Node.js", "MongoDB", "Python"} # Ada 2 "Python"
set_b = {"C++", "Python", "Java", "React"}

print("Set A (Duplikat otomatis hilang):", set_a)
print("Set B:", set_b)

# Operasi Himpunan
print("Union (|) - Gabungan semua:", set_a | set_b)
print("Intersection (&) - Yang ada di keduanya:", set_a & set_b)
print("Difference (-) - Ada di A tapi tidak di B:", set_a - set_b)
print("Symmetric Difference (^) - Yang tidak sama:", set_a ^ set_b)
print("\n")

# ==========================================
# 4. DICTIONARY - Key/Value Dasar
# ==========================================
print("--- 4. DICTIONARY ---")
# Dictionary memakai pasangan Kunci (Key) dan Nilai (Value)
mhs = {
    "nama": "Cindi Siregar",
    "nim": "12345678",
    "angkatan": 2023,
    "kota": "Medan"
}

# Operasi Dictionary
mhs["hobi"] = "Ngoding"     # Tambah key baru
mhs["angkatan"] = 2023      # Ubah nilai key
del mhs["kota"]             # Hapus key

print("Keys():", mhs.keys())
print("Values():", mhs.values())
print("Items():", mhs.items())

print("\nIterasi Key: Value ->")
for kunci, nilai in mhs.items():
    print(f"- {kunci}: {nilai}")
print("\n")

# ==========================================
# 5. NESTED STRUCTURES
# ==========================================
print("--- 5. NESTED STRUCTURES ---")
# List yang berisi banyak Dictionary
daftar_buku = [
    {"judul": "Dasar Pemrograman Web", "penulis": "Budi", "tahun": 2020},
    {"judul": "Kecerdasan Buatan AI", "penulis": "Andi", "tahun": 2025},
    {"judul": "Panduan React JS", "penulis": "Siti", "tahun": 2023},
    {"judul": "Algoritma C++", "penulis": "Joko", "tahun": 2018}
]

print("Semua Judul Buku:")
for buku in daftar_buku:
    print(f"- {buku['judul']}")

# Filter buku terbit >= 2023 dengan List Comprehension
buku_baru = [buku['judul'] for buku in daftar_buku if buku['tahun'] >= 2023]
print("Buku terbit >= 2023:", buku_baru)
print("\n")

# ==========================================
# 6. COMPREHENSION & UTILITAS
# ==========================================
print("--- 6. COMPREHENSION ---")
# List Comprehension
angka_genap = [x for x in range(1, 21) if x % 2 == 0]
angka_kuadrat = [x**2 for x in range(1, 21)]
print("List Genap (1-20):", angka_genap)
print("List Kuadrat (1-20):", angka_kuadrat)

# Dict Comprehension
dict_genap_ganjil = {x: ("Genap" if x % 2 == 0 else "Ganjil") for x in range(1, 11)}
print("Dict Genap/Ganjil:", dict_genap_ganjil)

# Set Comprehension
kalimat = "Semangat Belajar"
huruf_unik = {huruf.lower() for huruf in kalimat if huruf != " "}
print("Set Huruf Unik:", huruf_unik)
print("\n")

# ==========================================
# 7. KEANGGOTAAN & PENCARIAN SEDERHANA
# ==========================================
print("--- 7. KEANGGOTAAN ---")
# Cek keanggotaan (in)
cek_python = "Python" in set_a
print(f"Apakah 'Python' ada di Set A? {cek_python}")

# Gunakan index()
posisi_uisu = data_campuran.index("UISU")
print(f"Kata 'UISU' berada di dalam List pada indeks ke-{posisi_uisu}")
                     