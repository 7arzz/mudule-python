# ===== Type Data Dasar =====
data_integer = 1
print("data : ", data_integer)
print("- type : ", type(data_integer))

data_float = 1.5
print("data : ", data_float)
print("- type : ", type(data_float))

data_string = "Hello World"
print("data : ", data_string)
print("- type : ", type(data_string))

data_bool = True
print("data : ", data_bool)
print("- type : ", type(data_bool))

# ===== Type Data Khusus =====
data_complex = complex(5, 6)
print("data : ", data_complex)
print("- type : ", type(data_complex))

# ===== Type Data Dari Bahasa C =====
from ctypes import c_double, c_char

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- type : ", type(data_c_double))


# ======================================================
# Latihan Module 2
# ======================================================

print("Praktikum Algoritma dan Pemrograman 1 - Variable dan Tipe Data")

# Boolean
nilai_bool = False
print(nilai_bool)
print(type(nilai_bool))

# String
teks = "Ini adalah tulisan berupa String"
print(teks)

# Integer
angka_int = 100
print(angka_int)

# Float
angka_float = 0.001
print(angka_float)

# Hexadecimal
hex_value = 0x01
print(f"bilangan desimal dari 0x01 adalah {hex_value}")

# Octal → 0o12 = 10 desimal
oct_value = 0o12
print(oct_value)

# Complex numbers
kompleks1 = complex(2, 6)
print(type(kompleks1))
print(kompleks1)

kompleks2 = 2 + 6j
print(type(kompleks2))

# List of numbers
deret = list(range(96, 101))
print(deret)

# List of strings
angka_teks = ['seratus', 'dua ratus', 'tiga ratus']
print(angka_teks)

# Dictionary
data = {"nama": "Ani", "umur": 19}
print(data)

# String containing single quote
teks_quote = "This string contains a single quote (') character."
print(teks_quote)
