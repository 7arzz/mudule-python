# ============================
# Contoh 1: Fungsi print string
# ============================

def printme(text):
    "Mencetak string yang dikirim ke fungsi"
    print(text)
    return


# ================================
# Contoh 2: Penjumlahan barisan angka
# ================================

def jumlah(angka):
    total = 0
    for x in angka:
        total += x
    return total


# ===========================
# Contoh 3: Cek ganjil/genap
# ===========================

def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        print("genap")
    else:
        print("ganjil")
    return


# ================================
# Contoh 4: Menghitung rata-rata
# ================================

def rata_rata(a, b, c):
    return (a + b + c) / 3


# ================================
# Contoh 5: Kalkulator Sederhana
# ================================

def kalkulator(angka1, angka2):
    print("Hasil Penjumlahan :", angka1 + angka2)
    print("Hasil Pengurangan :", angka1 - angka2)
    print("Hasil Perkalian   :", angka1 * angka2)
    print("Hasil Pembagian   :", angka1 / angka2)


# ===============================
# Bagian Testing / Contoh Output
# ===============================

if __name__ == "__main__":

    print("== Contoh 1 ==")
    printme("hello world")

    print("\n== Contoh 2 ==")
    print("jumlah:", jumlah((8, 3, 1, 4, 5)))

    print("\n== Contoh 3 ==")
    cek_ganjil_genap(5)

    print("\n== Contoh 4 ==")
    print("Rata-rata:", rata_rata(1, 2, 3))

    print("\n== Contoh 5 ==")
    kalkulator(1, 2)
    
    
    # ===========================================
    # latihan Module 10
    # ============================================

# ============================================
# Program A: Menghitung Faktorial dengan Fungsi
# ============================================

def faktorial(n):
    hasil = 1
    urai = ""  # Untuk menampilkan bentuk perkalian (1x2x3...)
    for i in range(1, n + 1):
        hasil *= i
        urai += str(i)
        if i < n:
            urai += " x "
    return hasil, urai


# ==========================================================
# Program B: Menampilkan huruf Uppercase & Lowercase dari String
# ==========================================================

def hitung_upper_lower(teks):
    upper = 0
    lower = 0

    for char in teks:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower


# ============================================
# Program C: Segitiga Pascal (Pascal’s Triangle)
# ============================================

def pascal_triangle(n):
    segitiga = []

    for i in range(n):
        baris = [1] * (i + 1)
        for j in range(1, i):
            baris[j] = segitiga[i - 1][j - 1] + segitiga[i - 1][j]
        segitiga.append(baris)

    return segitiga


# ================================================================
# Program D: Mengembalikan list baru dari input list, setiap elemen dikali dirinya sendiri
# ================================================================

def kuadrat_list(data):
    hasil = []
    for x in data:
        hasil.append(x * x)
    return hasil


# ============================================
# Bagian Eksekusi Program (Testing)
# ============================================

if __name__ == "__main__":

    # Program A
    print("=== Program A: Faktorial ===")
    angka = int(input("Masukkan angka: "))
    hasil, bentuk = faktorial(angka)
    print(f"{bentuk} = {hasil}")

    # Program B
    print("\n=== Program B: Uppercase & Lowercase ===")
    teks = input("Masukkan sebuah kalimat: ")
    upper, lower = hitung_upper_lower(teks)
    print("Jumlah huruf kapital :", upper)
    print("Jumlah huruf kecil   :", lower)

    # Program C
    print("\n=== Program C: Segitiga Pascal ===")
    n = int(input("Masukkan jumlah baris segitiga pascal: "))
    triangle = pascal_triangle(n)
    for row in triangle:
        print(row)

    # Program D
    print("\n=== Program D: Kuadrat List ===")
    data = []
    jumlah = int(input("Berapa banyak angka? "))
    for i in range(jumlah):
        nilai = int(input(f"Angka ke-{i+1}: "))
        data.append(nilai)

    print("List awal :", data)
    print("List kuadrat :", kuadrat_list(data))
