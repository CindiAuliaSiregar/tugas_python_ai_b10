import numpy as np
import pandas as pd
import os

# Set seed agar hasil acak konsisten
np.random.seed(42)

# ==========================================
# 1. NUMPY - Data & Statistik
# ==========================================

nilai_ujian = np.random.randint(50, 101, size=10)

rata_rata = np.mean(nilai_ujian)
median = np.median(nilai_ujian)
std_dev = np.std(nilai_ujian)
nilai_min = np.min(nilai_ujian)
nilai_max = np.max(nilai_ujian)

# ==========================================
# 2. PANDAS - DataFrame
# ==========================================
data = {
    "nama": ["Cindi", "Aulia", "Tia", "Budi", "Siti"],
    "nim": ["712301", "712302", "712303", "712304", "712305"],
    "nilai": nilai_ujian[:5]  
}

df = pd.DataFrame(data)

# Menambahkan kolom status
df['status'] = df['nilai'].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

# ==========================================
# 3. OOP - GradeBook
# ==========================================
class GradeBook:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    def average(self) -> float:
        return self.df['nilai'].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = self.df[self.df['nilai'] >= threshold]
        return (len(lulus) / len(self.df)) * 100

    def save_summary(self, path: str):
        with open(path, 'w') as f:
            f.write("=== RINGKASAN TUGAS 6 ===\n")
            f.write(f"Rata-rata (NumPy): {rata_rata}\n")
            f.write(f"Median: {median}\n")
            f.write(f"Standar Deviasi: {std_dev:.2f}\n")
            f.write(f"Nilai Min/Max: {nilai_min}/{nilai_max}\n")
            f.write("-" * 25 + "\n")
            f.write(f"Jumlah Baris Data: {len(self.df)}\n")
            f.write(f"Jumlah LULUS: {len(self.df[self.df['status'] == 'LULUS'])}\n")
            f.write(f"Jumlah TIDAK LULUS: {len(self.df[self.df['status'] == 'TIDAK LULUS'])}\n")
            f.write(f"Persentase Kelulusan: {self.pass_rate():.2f}%\n")

    def __str__(self):
        return f"GradeBook(Data: {len(self.df)}, Rata-rata: {self.average():.2f})"

# ==========================================
# 4. DEMO
# ==========================================
if __name__ == "__main__":
    print("=== NUMPY ===")
    print(f"Array Nilai: {nilai_ujian}")
    print(f"Rata-rata: {rata_rata}, Median: {median}, Std Dev: {std_dev:.2f}")
    
    print("\n=== PANDAS ===")
    print(df.head())
    
    print("\n=== OOP: GRADEBOOK ===")
    book = GradeBook(df)
    print(book)
    print(f"Average: {book.average()}")
    print(f"Pass Rate: {book.pass_rate()}%")
    
    # Simpan ke file teks
    file_name = "ringkasan_tugas6.txt"
    book.save_summary(file_name)
    print(f"\n[Selesai] Ringkasan telah disimpan di {file_name}")