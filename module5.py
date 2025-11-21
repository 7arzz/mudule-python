# ================================================
# 1. IF SEDERHANA
# ================================================
angka = 10

if angka > 5:
    print("IF Sederhana: angka lebih besar dari 5")


# ================================================
# 2. IF – ELSE
# ================================================
umur = 15

if umur >= 17:
    print("IF-ELSE: Boleh membuat KTP")
else:
    print("IF-ELSE: Belum boleh membuat KTP")


# ================================================
# 3. IF – ELIF – ELSE
# ================================================
nilai = 85

if nilai >= 90:
    print("IF-ELIF-ELSE: Nilai A")
elif nilai >= 75:
    print("IF-ELIF-ELSE: Nilai B")
elif nilai >= 60:
    print("IF-ELIF-ELSE: Nilai C")
else:
    print("IF-ELIF-ELSE: Nilai D")


# ================================================
# 4. IF BERSARANG (NESTED IF)
# ================================================
username = "tarzz"
password = "12345"

if username == "tarzz":
    if password == "12345":
        print("Nested IF: Login sukses")
    else:
        print("Nested IF: Password salah")
else:
    print("Nested IF: Username tidak ditemukan")


# ================================================
# 5. KONDISI GABUNGAN (AND, OR)
# ================================================
umur = 18
punya_sim = True

# syarat: umur >= 17 DAN punya SIM
if umur >= 17 and punya_sim:
    print("AND: Boleh mengemudi")

# syarat: umur < 17 ATAU tidak punya SIM
if umur < 17 or not punya_sim:
    print("OR: Tidak boleh mengemudi")


# ================================================
# 6. SHORT HAND IF (ONE LINE IF)
# ================================================
x = 10
print("Short hand IF:", "besar" if x > 5 else "kecil")

# bentuk panjang: print("besar") if x > 5 else print("kecil")


# ================================================
# 7. MULTI-KONDISI DALAM SATU BARIS
# ================================================
y = 0
hasil = "positif" if y > 0 else "negatif" if y < 0 else "nol"
print("Multi-kondisi:", hasil)


# ================================================
# 8. IF DENGAN ANGGAPAN BOOLEAN
# ================================================
is_active = True

if is_active:
    print("Boolean IF: User aktif")
else:
    print("Boolean IF: User tidak aktif")


# ================================================
# 9. IF UNTUK CEK KEANGGOTAAN (IN)
# ================================================
huruf = 'a'

if huruf in "aiueo":
    print("IN: Huruf vokal")
else:
    print("IN: Huruf konsonan")


# ================================================
# 10. IF UNTUK CEK DATA DI LIST
# ================================================
buah = ["apel", "jeruk", "mangga"]

if "jeruk" in buah:
    print("List IN: Jeruk ada di dalam list")
else:
    print("List IN: Tidak ditemukan")


# ================================================
# 11. MATCH–CASE (PYTHON 3.10+) MIRIP SWITCH CASE
# ================================================
menu = 2

match menu:
    case 1:
        print("Match: Menu 1 dipilih")
    case 2:
        print("Match: Menu 2 dipilih")
    case 3:
        print("Match: Menu 3 dipilih")
    case _:
        print("Match: Menu tidak ditemukan")

# =====================================================
# Latihan Module 5
# ====================================================


# =====================================================
# PROGRAM 1: DETEKSI JENIS SEGITIGA
# =====================================================

print("=== Program Deteksi Jenis Segitiga ===")

x = int(input("Masukkan panjang sisi x: "))
y = int(input("Masukkan panjang sisi y: "))
z = int(input("Masukkan panjang sisi z: "))

if x == y == z:
    print("Semua sisi sama → Segitiga Sama Sisi (equilateral triangle)")
elif x == y or x == z or y == z:
    print("Dua sisi sama → Segitiga Sama Kaki (isosceles triangle)")
else:
    print("Tidak ada sisi yang sama → Segitiga Sembarang (scalene triangle)")


# =====================================================
# PROGRAM 2: DETEKSI TAHUN KABISAT
# =====================================================

print("\n=== Program Deteksi Tahun Kabisat ===")

tahun = int(input("Masukkan tahun: "))

if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(tahun, "→ Merupakan tahun kabisat")
else:
    print(tahun, "→ Bukan tahun kabisat")


# =====================================================
# PROGRAM 3: DETEKSI ZODIAK YUNANI
# =====================================================

print("\n=== Program Deteksi Zodiak Yunani ===")

tanggal = int(input("Masukkan tanggal lahir: "))
bulan = int(input("Masukkan bulan lahir (1-12): "))

if (tanggal >= 21 and bulan == 3) or (tanggal <= 19 and bulan == 4):
    zodiak = "Aries"
elif (tanggal >= 20 and bulan == 4) or (tanggal <= 20 and bulan == 5):
    zodiak = "Taurus"
elif (tanggal >= 21 and bulan == 5) or (tanggal <= 20 and bulan == 6):
    zodiak = "Gemini"
elif (tanggal >= 21 and bulan == 6) or (tanggal <= 22 and bulan == 7):
    zodiak = "Cancer"
elif (tanggal >= 23 and bulan == 7) or (tanggal <= 22 and bulan == 8):
    zodiak = "Leo"
elif (tanggal >= 23 and bulan == 8) or (tanggal <= 22 and bulan == 9):
    zodiak = "Virgo"
elif (tanggal >= 23 and bulan == 9) or (tanggal <= 22 and bulan == 10):
    zodiak = "Libra"
elif (tanggal >= 23 and bulan == 10) or (tanggal <= 21 and bulan == 11):
    zodiak = "Scorpio"
elif (tanggal >= 22 and bulan == 11) or (tanggal <= 21 and bulan == 12):
    zodiak = "Sagittarius"
elif (tanggal >= 22 and bulan == 12) or (tanggal <= 19 and bulan == 1):
    zodiak = "Capricorn"
elif (tanggal >= 20 and bulan == 1) or (tanggal <= 18 and bulan == 2):
    zodiak = "Aquarius"
elif (tanggal >= 19 and bulan == 2) or (tanggal <= 20 and bulan == 3):
    zodiak = "Pisces"
else:
    zodiak = "Tanggal tidak valid"

print("Zodiak Anda adalah:", zodiak)

# =====================================================
# PROGRAM 4: DETEKSI ZODIAK CINA (SHIO)
# =====================================================

print("\n=== Program Deteksi Zodiak Cina ===")

tahun = int(input("Masukkan tahun lahir Anda: "))

shio_list = [
    "Tikus", "Kerbau", "Harimau", "Kelinci",
    "Naga", "Ular", "Kuda", "Kambing",
    "Monyet", "Ayam", "Anjing", "Babi"
]

# Rumus: (tahun lahir - 4) % 12
index = (tahun - 4) % 12

print("Shio Anda adalah:", shio_list[index])
