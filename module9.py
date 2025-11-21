# ======================================================
#     MATERI TUPLE & DICTIONARY – FULL CONTOH PYTHON
# ======================================================

print("=== TUPLE ===")

# -------------------------------
# Program 1 – Membuat Tuple
# -------------------------------
print("\nProgram 1: Membuat Tuple")
tup1 = ('sistem komputer', 'teknik informatika', 2008, 2017)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

print(tup1)
print(tup2)
print(tup3)

# Tuple kosong
t_kosong = ()
print("Tuple kosong:", t_kosong)

# Tuple 1 elemen (HARUS pakai koma)
t_satu = (50,)
print("Tuple 1 elemen:", t_satu)


# -------------------------------
# Program 2 – Akses Nilai Tuple
# -------------------------------
print("\nProgram 2: Akses Tuple")

tupA = ('sistem komputer', 'teknik informatika', 2008, 2017)
tupB = (1, 2, 3, 4, 5, 6, 7)

print("tupA[0]:", tupA[0])
print("tupB[1:5]:", tupB[1:5])


# -------------------------------
# Program 3 – Update Tuple (tidak bisa, jadi membuat baru)
# -------------------------------
print("\nProgram 3: Update Tuple dengan Membuat Tuple Baru")

tupX = (12, 34.56)
tupY = ('abc', 'xyz')

tupZ = tupX + tupY  # gabung membuat tuple baru
print("Tuple gabungan:", tupZ)


# -------------------------------
# Program 4 – Hapus Tuple
# -------------------------------
print("\nProgram 4: Hapus Tuple")

tup4 = ('fisika', 'kimia', 1993, 2017)
print("Sebelum hapus:", tup4)
del tup4

print("Setelah hapus tuple: (akan error jika dicetak)")
try:
    print(tup4)
except NameError:
    print("ERROR: tup4 sudah dihapus!")


# -------------------------------
# Program 5 – Operasi Dasar Tuple
# -------------------------------
print("\nProgram 5: Operasi Dasar Tuple")

T = ('C++', 'Java', 'Python')

print("Length:", len(T))
print("Concatenate:", (1, 2, 3) + (4, 5, 6))
print("Repetition:", ('Halo!',) * 4)
print("Membership 3 in (1,2,3):", 3 in (1, 2, 3))

print("Indexing T[2]:", T[2])
print("Indexing T[-2]:", T[-2])
print("Slicing T[1:]:", T[1:])


# ======================================================
#                      DICTIONARY
# ======================================================
print("\n=== DICTIONARY ===")

# -------------------------------
# Program 6 – Akses Dictionary
# -------------------------------
print("\nProgram 6: Akses Dictionary")

dictA = {'Name': 'Luffy', 'Age': 7, 'Class': 'First'}
print("Name:", dictA['Name'])
print("Age:", dictA['Age'])


# -------------------------------
# Program 7 – Update Dictionary
# -------------------------------
print("\nProgram 7: Update Dictionary")

dictB = {'Name': 'Luffy', 'Age': 7, 'Class': 'First'}
dictB['Age'] = 8
dictB['School'] = "Marijoa School"

print(dictB)


# -------------------------------
# Program 8 – Hapus Dictionary
# -------------------------------
print("\nProgram 8: Hapus Dictionary")

dictC = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("Sebelum hapus:", dictC)

del dictC['Name']
dictC.clear()
del dictC

print("Dictionary dihapus, mencoba mengakses...")
try:
    print(dictC)
except:
    print("ERROR: dictC sudah dihapus lengkap!")


# -------------------------------
# Program 9 – Built-in Dictionary
# -------------------------------
print("\nProgram 9: Built-in Dictionary")

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dicGabung = {}

for d in (dic1, dic2, dic3):
    dicGabung.update(d)

print("Gabungan:", dicGabung)


# -------------------------------
# Program 10 – Cek Angka dalam Dictionary
# -------------------------------
print("\nProgram 10: Cek Key dalam Dictionary")

d = {1: 10, 2: 20, 3: 30}
cek = 3

if cek in d:
    print(cek, "tersedia dalam dictionary")
else:
    print(cek, "tidak tersedia")


# -------------------------------
# Program 11 – Gabungkan Dua Dictionary
# -------------------------------
print("\nProgram 11: Gabungkan Dictionary")

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 400}

gabung = d1.copy()
gabung.update(d2)

print("Hasil gabungan:", gabung)


# ============================
# Latihan Module 8
# ============================

print("\n=== a. Tuple ke String ===")
# a. Program menampilkan isi tuple lalu mengonversi ke string
my_tuple = ("Joni", 15, "Sidoarjo")
print("Data tuple:", my_tuple)

tuple_to_string = " ".join([str(i) for i in my_tuple])
print("Setelah dikonversi ke string:", tuple_to_string)


print("\n=== b. Penjumlahan nilai dalam Dictionary ===")
# b. Menjumlahkan nilai pada dictionary
nilai_mapel = {
    "MTK": 90,
    "IPA": 85,
    "IPS": 88,
    "B. Indo": 92
}

print("Dictionary:", nilai_mapel)
jumlah = sum(nilai_mapel.values())
print("Total jumlah nilai:", jumlah)


print("\n=== c. Perkalian nilai dari Dictionary ===")
# c. Mengalikan semua nilai dalam dictionary
angka_dict = {
    "a": 3,
    "b": 5,
    "c": 2,
    "d": 4
}

hasil_kali = 1
for v in angka_dict.values():
    hasil_kali *= v

print("Dictionary:", angka_dict)
print("Hasil perkalian semua nilai:", hasil_kali)


print("\n=== d. Hapus key dari Dictionary ===")
# d. Menghapus key dan menampilkan perubahan
data_awal = {
    "nama": "Tarzz",
    "kelas": "9",
    "sekolah": "SMPN 2 Sukodono",
    "hobi": "Ngoding"
}

print("Dictionary awal:", data_awal)

# hapus satu key
data_baru = data_awal.copy()
del data_baru["hobi"]

print("Dictionary setelah dihapus:", data_baru)


print("\n=== e. Game Tebak Nama Binatang ===")
# e. Game tebak-tebakan English → Indonesian

hewan = {
    "Ant": "Semut",
    "Bee": "Lebah",
    "Mosquito": "Nyamuk",
    "Butterfly": "Kupu-kupu",
    "Spider": "Laba-laba",
    "Fly": "Lalat",
    "Hedgehog": "Landak",
    "Snail": "Siput"
}

print("Tebak arti nama hewan (Inggris → Indonesia)!")
import random

# pilih random 1 hewan
random_key = random.choice(list(hewan.keys()))
jawaban = input(f"Apa bahasa Indonesianya '{random_key}'? : ")

if jawaban.lower() == hewan[random_key].lower():
    print("Benar! 🎉")
else:
    print(f"Salah! Jawaban yang benar adalah: {hewan[random_key]}")
