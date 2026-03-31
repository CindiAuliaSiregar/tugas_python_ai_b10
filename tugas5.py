# ==========================================
# 1. FUNCTION (Fungsi)
# ==========================================

# Fungsi menyapa
def greet(nama: str) -> str:
    return f"Halo, {nama}!"

# Fungsi menambah angka (b disetel 0.0 jika tidak diisi)
def tambah(a: float, b: float = 0.0) -> float:
    return a + b

# Fungsi mencari rata-rata
def rata_rata(angka: list[float]) -> float:
    if not angka:  # Jika list kosong
        return 0.0
    # Hitung rata-rata dan bulatkan 2 angka di belakang koma
    hasil = sum(angka) / len(angka)
    return round(hasil, 2)


# ==========================================
# 2. CLASS (Kelas)
# ==========================================

class Student:
    # Ini adalah tampilan awal saat mahasiswa baru dibuat
    def __init__(self, nama: str, nim: str):
        self.nama = nama
        self.nim = nim
        self.nilai: list[float] = []  # List nilai awalnya kosong

    # Method untuk menambah nilai ke dalam list
    def tambah_nilai(self, skor: float):
        self.nilai.append(skor)

    # Method untuk menghitung rata-rata nilai mahasiswa ini
    def rata_nilai(self) -> float:
        # Memanggil fungsi rata_rata() yang ada di atas tadi
        return rata_rata(self.nilai)

    # Method untuk mengecek status lulus (KKM = 70.0)
    def status(self, threshold: float = 70.0) -> str:
        if self.rata_nilai() >= threshold:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    # Method untuk mencetak bentuk ringkas dari data mahasiswa
    def __str__(self):
        return f"Student(nama='{self.nama}', nim='{self.nim}', rata={self.rata_nilai()}, status={self.status()})"


# ==========================================
# 3. DEMO (Sesuai Instruksi Tugas)
# ==========================================

if __name__ == "__main__":
    
    print("=== FUNCTIONS ===")
    # Memanggil dan mencetak hasil fungsi
    print(greet("Arifian"))
    print("Hasil tambah(5, 7) :", tambah(5, 7))
    print("Hasil tambah(10)   :", tambah(10))
    print("Rata-rata [80, 90, 100] :", rata_rata([80, 90, 100]))
    print("Rata-rata []            :", rata_rata([]))
    print("\n")
    
    print("=== CLASS STUDENT ===")
    mhs1 = Student("Cindi Siregar", "12345678")
    mhs1.tambah_nilai(85.5)
    mhs1.tambah_nilai(90.0)
    mhs1.tambah_nilai(95.0)

    mhs2 = Student("Budi", "A123")
    mhs2.tambah_nilai(60.0)
    mhs2.tambah_nilai(65.0)

    # Cetak objek (otomatis memanggil method __str__)
    print("Data Mahasiswa 1:")
    print(mhs1)
    
    print("\nData Mahasiswa 2:")
    print(mhs2)