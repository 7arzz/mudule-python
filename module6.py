print("===== LOOPING LENGKAP PYTHON =====")

# ============================
# 1. FOR LOOP DASAR
# ============================
print("\n1. For Loop Dasar")
for i in range(5):
    print("Perulangan ke-", i)


# ============================
# 2. FOR LOOP (MENGAKSES LIST)
# ============================
print("\n2. For Loop dengan List")
buah = ["apel", "jeruk", "mangga"]
for item in buah:
    print("Buah:", item)


# ============================
# 3. FOR LOOP DENGAN RANGE
# ============================
print("\n3. Range (start, stop, step)")
for i in range(1, 11, 2):
    print("Angka:", i)


# ============================
# 4. NESTED LOOP (FOR DALAM FOR)
# ============================
print("\n4. Nested Loop")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# ============================
# 5. WHILE LOOP DASAR
# ============================
print("\n5. While Loop")
x = 0
while x < 5:
    print("x =", x)
    x += 1


# ============================
# 6. WHILE LOOP (BREAK)
# ============================
print("\n6. While + Break")
y = 0
while True:
    if y == 3:
        break
    print("y =", y)
    y += 1


# ============================
# 7. FOR LOOP (BREAK)
# ============================
print("\n7. For + Break")
for i in range(10):
    if i == 4:
        break
    print("i =", i)


# ============================
# 8. CONTINUE (LEWATI ITERASI)
# ============================
print("\n8. Continue")
for i in range(6):
    if i == 3:
        continue  # skip angka 3
    print("i =", i)


# ============================
# 9. ELSE DALAM LOOP (KHUSUS PYTHON)
# ============================
print("\n9. Loop + Else")
for i in range(5):
    print("angka:", i)
else:
    print("Loop selesai tanpa break")


# ============================
# 10. ELSE TIDAK JALAN KARNA BREAK
# ============================
print("\n10. Loop + Else (tapi break)")
for i in range(5):
    if i == 2:
        break
    print("angka:", i)
else:
    print("Ini tidak akan muncul")


# ============================
# 11. LOOPING DICTIONARY
# ============================
print("\n11. Loop Dictionary")
orang = {"nama": "Tarzz", "umur": 14, "hobi": "ngoding"}
for key, value in orang.items():
    print(key, ":", value)


# ============================
# 12. LOOPING STRING
# ============================
print("\n12. Loop String")
for huruf in "TARZZ":
    print("Huruf:", huruf)


# ============================
# 13. LOOPING DENGAN ENUMERATE
# ============================
print("\n13. Enumerate (index + nilai)")
for index, item in enumerate(["A", "B", "C"]):
    print(index, item)


# ============================
# LATIHAN MODULE 6
# ============================

# =====================================================
# Program 1: Filter bilangan genap dan ganjil versi input user
# =====================================================

print("=== Program Filter Genap & Ganjil ===")

# User input angka (dipisahkan dengan spasi jangan pakai koma)
data_input = input("Masukkan beberapa angka (pisahkan dengan spasi): ")

# Ubah input string menjadi list bilangan integer
data = list(map(int, data_input.split()))

genap = []
ganjil = []

# --- Menggunakan For Loop ---
for angka in data:
    if angka % 2 == 0:
        genap.append(angka)
    else:
        ganjil.append(angka)

print("\nData awal:", data)
print("Bilangan genap :", genap, "Jumlah =", len(genap))
print("Bilangan ganjil:", ganjil, "Jumlah =", len(ganjil))

# --- Nested Loop untuk menampilkan dalam bentuk tabel ---
print("\n=== Tabel Kategori ===")
kategori = [("Genap", genap), ("Ganjil", ganjil)]

for nama, isi in kategori:
    print(f"\n{nama}:")
    i = 0
    while i < len(isi):
        print(f"- {isi[i]}")
        i += 1

# =====================================================
# Program 2: Tabel perkalian dari input
# =====================================================

n = int(input("Masukkan angka: "))

print(f"\nTabel Perkalian {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Versi while loop
print("\nVersi While:")
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# =====================================================
# Program 3: Deret Fibonacci
# =====================================================

jumlah = int(input("Masukkan jumlah bilangan Fibonacci: "))

a, b = 0, 1
fibo = []

# Menggunakan For Loop
for _ in range(jumlah):
    fibo.append(a)
    a, b = b, a + b

print("\nDeret Fibonacci (for loop):")
print(fibo)

# Menggunakan While Loop
print("\nDeret Fibonacci (while loop):")
x, y = 0, 1
i = 0
hasil = []
while i < jumlah:
    hasil.append(x)
    x, y = y, x + y
    i += 1
print(hasil)

# Nested loop untuk tampilan baris per baris
print("\nOutput satu per satu:")
for angka in fibo:
    for _ in range(1):  
        print(angka)


# =====================================================
# Program 4: Perkalian 1–100
# =====================================================

print("Perkalian nilai 1–100:")

# Menggunakan For Loop
for i in range(1, 101):
    print(f"3 x {i} = {3 * i}")

# Menggunakan While Loop
print("\nVersi While:")
i = 1
while i <= 100:
    print(f"3 x {i} = {3 * i}")
    i += 1
