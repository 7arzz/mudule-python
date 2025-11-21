# Materi Lengkap Number, String, Math, Random, Trigonometri di Python

import math
import random

print("===== 1. NUMBER =====")

# Integer
int_a = 20
int_b = -13
print("Int:", int_a, int_b)

# Float
float_a = 1.20
float_b = -32.52e10
print("Float:", float_a, float_b)

# Complex
complex_a = 3 + 5j
print("Complex:", complex_a)

print("\n===== 2. KONVERSI NUMBER =====")
num = 12.7
print("int():", int(num))
print("float():", float(num))
print("complex():", complex(num))
print("complex(x, y):", complex(3, 4))

print("\n===== 3. FUNGSI MATH =====")
x = -15.7
print("abs():", abs(x))
print("ceil():", math.ceil(x))
print("floor():", math.floor(x))
print("exp(2):", math.exp(2))
print("log(10):", math.log(10))
print("log10(10):", math.log10(10))
print("max():", max(3,5,9))
print("min():", min(3,5,9))
print("modf():", math.modf(4.67))
print("pow(2,3):", pow(2,3))
print("round(4.678, 2):", round(4.678,2))
print("sqrt(81):", math.sqrt(81))

print("\n===== 4. RANDOM =====")
data = [1,2,3,4,5]
print("choice():", random.choice(data))
print("randrange():", random.randrange(1, 10, 2))
print("random():", random.random())
random.seed(5)
print("seed(5) -> random():", random.random())
random.shuffle(data)
print("shuffle():", data)
print("uniform(1,5):", random.uniform(1,5))

print("\n===== 5. TRIGONOMETRI =====")
angle = math.radians(60)
print("cos(60°):", math.cos(angle))
print("sin(60°):", math.sin(angle))
print("tan(60°):", math.tan(angle))
print("degrees():", math.degrees(angle))
print("hypot(3,4):", math.hypot(3,4))

print("\n===== 6. KONSTANTA =====")
print("pi:", math.pi)
print("e:", math.e)

print("\n===== 7. STRING =====")
s = "Hello World"
print(s[0])
print(s[1:5])
print(s[:6] + "Python")

print("\n===== 8. ESCAPE CHARACTER =====")
print("Baris baru -> \nHello")
print("Tab -> \tHello")
print("Backslash -> \\")
print("Quote: \"Hello\"")

print("\n===== 9. OPERATOR STRING =====")
print("Concat:", "Hello " + "Python")
print("Repeat:", "Hi " * 3)
print("Check 'He' in 'Hello':", "He" in "Hello")

print("\n===== 10. FORMAT STRING % =====")
print("Nama %s umur %d" % ("Zara", 21))

print("\n===== 11. TRIPLE QUOTE =====")
text = """Ini string
multi baris
dengan TAB -> \t dan newline -> \n"""
print(text)

print("\n===== 12. METODE STRING =====")
st = "   python STRING Test 123   "
print("upper():", st.upper())
print("lower():", st.lower())
print("title():", st.title())
print("isdigit():", st.isdigit())
print("split():", st.split())
print("strip():", st.strip())
print("replace():", st.replace("python", "PY"))
print("find('STRING'):", st.find("STRING"))


# ======================================================
# Latihan Module 7
# ======================================================


print("=== Modul 7: Numbers & String ===\n")

# ==========================================
# a. STRING ARRAYS (INDEXING)
# ==========================================
a = "Hello World"

print("a. STRING ARRAYS")
print("String:", a)
print("Index 2:", a[2])
print("Index 4:", a[4])
print("Index 8:", a[8])
print("Index 10:", a[10])
print()

# ==========================================
# b. STRING RANGE (SLICING)
# ==========================================
a = "Hello World"

print("b. STRING SLICING")
print("String asli:", a)
print("a[0:5]  ->", a[0:5])     # Hello
print("a[6:11] ->", a[6:11])    # World
print("a[:5]   ->", a[:5])
print("a[6:]   ->", a[6:])
print()

# ==========================================
# c. LOWERCASE, UPPERCASE, REPLACE
# ==========================================
a = "Hello World"

print("c. LOWERCASE, UPPERCASE, REPLACE")
print("Lowercase :", a.lower())
print("Uppercase :", a.upper())
print("Replace 'o' -> '0':", a.replace('o', '0'))
print()

# ==========================================
# d. CAESAR CIPHER ENCRYPTION
# ==========================================
alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_encrypt(text, shift):
    hasil = ""
    for char in text.lower():
        if char in alphabet:
            index_baru = (alphabet.index(char) + shift) % 26
            hasil += alphabet[index_baru]
        else:
            hasil += char
    return hasil

print("d. CAESAR CIPHER ENCRYPTION")
teks = "hello world"
shift = 3

print("Teks asli   :", teks)
print("Shift       :", shift)
print("Terenkripsi :", caesar_encrypt(teks, shift))