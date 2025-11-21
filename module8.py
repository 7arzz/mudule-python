# ======================================================
# Contoh sederhana pembuatan list dalam Python
# ======================================================
list1 = ['sistem komputer', 'teknik informatika', 2008, 2020]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]

print(list1)
print(list2)
print(list3)

# ======================================================
# akses nilai dalam list
# ======================================================
list1 = ['sistem komputer', 'teknik informatika', 2008, 2020]
list2 = [1, 2, 3, 4, 5, 6, 7]

print("list1[0]:", list1[0])
print("list2[1:5]:", list2[1:5])  # slicing

# ======================================================
# Update Nilai Dalam List
# ======================================================
data = ['sistem komputer', 'teknik informatika', 2008, 2020]

print("Nilai index 2:", data[2])
data[2] = 2001
print("Nilai index 2 setelah update:", data[2])

# =====================================================
# Menghapus Nilai Dalam List
# =====================================================
data = ['sistem komputer', 'teknik informatika', 2008, 2020]

print("Sebelum dihapus:", data)
del data[2]   # hapus berdasarkan index
print("Setelah dihapus:", data)


# =====================================================
# Operasi Dasar Pada List
# =====================================================
print(len([1, 2, 3, 4]))                  # 4
print([1, 2, 3] + [4, 5, 6])              # concatenation
print(['Halo!'] * 4)                      # repetition
print(2 in [1, 2, 3])                     # membership

# =====================================================
# Iterasi list
# =====================================================
for x in [1, 2, 3]:
    print(x, end=" ")


# =====================================================
# Indexing, Slicing, Matrix
# =====================================================
L = ['C++', 'Java', 'Python']

print(L[2])     # Python
print(L[-2])    # Java
print(L[1:])    # ['Java', 'Python']

# =====================================================
# Method & Fungsi Built-in Pada List
# =====================================================
data = [5, 2, 9, 1]

data.append(15)       # tambah elemen
print(data)

print(data.count(2))  # hitung angka 2

data.extend([100, 200])  # tambah banyak elemen
print(data)

print(data.index(9))  # cari index angka 9

data.insert(1, 50)    # tambah 50 pada index 1
print(data)

data.pop()            # hapus elemen terakhir
print(data)

data.remove(50)       # hapus nilai 50
print(data)

data.reverse()        # balik list
print(data)

data.sort()           # urutkan
print(data)


# =====================================================
# Contoh Program List (Filter Genap & Ganjil)
# =====================================================
num = [-1, 2, 53, 5, 50, 153, 91, 87]

genap = [x for x in num if x % 2 == 0]
ganjil = [x for x in num if x % 2 != 0]

print("list angka:", num)
print("angka genap:", genap)
print("angka ganjil:", ganjil)

# =====================================================
# Menggabungkan List Menjadi String
# =====================================================
s = ['g', 'a', 'n', 't', 'e', 'n', 'g']
str1 = ''.join(s)
print(str1)




# =====================================================
# Latihan Module 8
# =====================================================


print("\n=== PROGRAM A: Nilai Maksimum dari List ===")
data = [12, 7, 25, 3, 19, 40, 2]

maksimum = data[0]
for angka in data:
    if angka > maksimum:
        maksimum = angka

print("List:", data)
print("Nilai maksimum:", maksimum)


# ============================================
print("\n=== PROGRAM B: Nilai Minimum dari List ===")
data2 = [12, 7, 25, 3, 19, 40, 2]

minimum = data2[0]
for angka in data2:
    if angka < minimum:
        minimum = angka

print("List:", data2)
print("Nilai minimum:", minimum)


# ============================================
print("\n=== PROGRAM C: Filter Kata <= 4 Huruf ===")
kata = ["kota", "rumah", "api", "meja", "kursi", "aku", "data"]
hasil = []

for item in kata:
    if len(item) <= 4:
        hasil.append(item)

print("List kata:", kata)
print("Kata dengan panjang <= 4 huruf:", hasil)


# ============================================
print("\n=== PROGRAM D: Menyisipkan Anggota Baru ===")
list_asli = [1, 2, 3, 4, 5]
anggota_baru = "X"
hasil_sisip = []

for item in list_asli:
    hasil_sisip.append(item)
    hasil_sisip.append(anggota_baru)

# Menghapus X terakhir agar tidak berlebihan
hasil_sisip.pop()

print("List asli:", list_asli)
print("List setelah disisipkan anggota baru:", hasil_sisip)


# ============================================
print("\n=== PROGRAM E: Caesar Cipher Decrypt ===")

def caesar_decrypt(text, shift):
    hasil = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            hasil += chr((ord(char) - base - shift) % 26 + base)
        else:
            hasil += char
    return hasil

ciphertext = "Khoor Zruog"   # contoh dari modul 7 (Hello World digeser 3)
shift = 3

plaintext = caesar_decrypt(ciphertext, shift)

print("Ciphertext:", ciphertext)
print("Shift:", shift)
print("Hasil decrypt:", plaintext)
