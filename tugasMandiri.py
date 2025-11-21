# ============================================
# GAME GUNTING BATU KERTAS
# ============================================
print("=== Game Gunting Batu Kertas (Sedikit absurd) ===")

def hasil(p1, p2):
    if p1 == p2:
        return "Seri"

    if (p1 == "gunting" and p2 == "kertas") or \
       (p1 == "batu" and p2 == "gunting") or \
       (p1 == "kertas" and p2 == "batu"):
        return "Pemain 1 Menang"
    else:
        return "Pemain 2 Menang"


while True:
    print("Pemain 1: Silahkan pilih (gunting, batu, kertas): ", end="")
    p1 = input()

    print("Pemain 2: Silahkan pilih (gunting, batu, kertas): ", end="")
    p2 = input()

    print(hasil(p1, p2))

    ulang = input("Main lagi? (y/t): ")
    if ulang.lower() != "y":
        break

print("Permainan selesai!")
# ============================================





# ============================================
# HITUNG JUMLAH HURUF & ANGKA
# ============================================
print("=== Hitung Huruf & Angka dari Kalimat ===")

text = input("Inputan: ")

huruf = 0
angka = 0

for x in text:
    if x.isalpha():
        huruf += 1
    elif x.isdigit():
        angka += 1

print("Jumlah Huruf :", huruf)
print("Jumlah Angka :", angka)
# ============================================



# ============================================
# SEGITIGA ANGKA
# ============================================
print("=== Segitiga Angka ===")

n = int(input("Masukkan angka: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# ============================================






# ============================================
# FILTER LIST YG HABIS DIBAGI 3 & <= 151
# ============================================

list1 = [13, 15, 30, 41, 45, 55, 75, 95, 102, 135, 139, 151, 193, 200]

print("""
      Angka yang habis dibagi 3 dan <=151: 
      dari list1 = [13, 15, 30, 41, 45, 55, 75, 95, 102, 135, 139, 151, 193, 200]
      """)

for x in list1:
    if x % 3 == 0 and x <= 151:
        print(x)
# ============================================