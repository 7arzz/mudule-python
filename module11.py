# ==========================================================
# MODULE 11 — OBJECT ORIENTED PROGRAMMING (OOP) — RANGKUMAN
# ==========================================================

# ----------------------------------------------------------
# 1. Contoh Class dengan Class Variable & Instance Variable
# ----------------------------------------------------------

class Employee:
    """Common base class for all employees"""
    empCount = 0  # Class Variable

    def __init__(self, name, salary):
        self.name = name      # Instance Variable
        self.salary = salary  # Instance Variable
        Employee.empCount += 1  # Mengupdate class variable

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name:", self.name, ", Salary:", self.salary)


# ----------------------------------------------------------
# 2. Contoh Membuat Object (Instance)
# ----------------------------------------------------------

# Membuat object Employee
emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee:", Employee.empCount)


# ----------------------------------------------------------
# 3. Contoh Class Sederhana Lainnya
# ----------------------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name   # Instance Variable
        self.age = age     # Instance Variable

    def myfunc(self):
        print("Halo nama saya:", self.name)
        print("Umur saya:", self.age)


# Membuat object Person
p1 = Person("Budi", 19)
p1.myfunc()


# ================================================================
# MODULE 11 — OBJECT & CLASS
# ================================================================

# ================================================================
# (a) PROGRAM DETAIL PERSONAL
# ================================================================

# Class for Computer Science Student  
class Person:

    # Class Variable  
    person = 'Person'

    # Constructor
    def __init__(self, rambut, warna):
        # Instance Variable
        self.rambut = rambut
        self.warna = warna


# Objects 
Budi = Person("Ikal", "Hitam")
Michael = Person("Pendek", "Coklat")

print("=== DETAIL PERSONAL ===")
print("Budi details:")
print("Rambut:", Budi.rambut)
print("Warna Rambut:", Budi.warna)

print("\nMichael details:")
print("Rambut:", Michael.rambut)
print("Warna Rambut:", Michael.warna)


# ================================================================
# (b) OOP VERSI PROGRAM MODUL 10
# (a) Faktorial
# (b) Uppercase / Lowercase Counter
# (c) Pascal Triangle
# (d) Kuadrat List
# ================================================================


# ===============================================================
# Latihan Module 11
# ================================================================

# -------------------------------
# Class A — Faktorial
# -------------------------------
class Faktorial:
    def __init__(self, angka):
        self.angka = angka
    
    def hitung(self):
        hasil = 1
        urai = ""
        for i in range(1, self.angka + 1):
            hasil *= i
            urai += str(i)
            if i < self.angka:
                urai += " x "
        return hasil, urai


# -------------------------------
# Class B — Upper & Lower Counter
# -------------------------------
class TextCounter:
    def __init__(self, text):
        self.text = text
    
    def count(self):
        upper = 0
        lower = 0
        for char in self.text:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
        return upper, lower


# -------------------------------
# Class C — Pascal Triangle
# -------------------------------
class PascalTriangle:
    def __init__(self, n):
        self.n = n
    
    def generate(self):
        segitiga = []
        for i in range(self.n):
            baris = [1] * (i + 1)
            for j in range(1, i):
                baris[j] = segitiga[i - 1][j - 1] + segitiga[i - 1][j]
            segitiga.append(baris)
        return segitiga


# -------------------------------
# Class D — Kuadrat List
# -------------------------------
class ListSquarer:
    def __init__(self, data):
        self.data = data
    
    def square(self):
        return [x * x for x in self.data]


# ================================================================
# BAGIAN EKSEKUSI
# ================================================================
print("\n=== FAKTORIAL ===")
f = Faktorial(5)
hasil, urai = f.hitung()
print(f"{urai} = {hasil}")

print("\n=== UPPER & LOWER CASE ===")
t = TextCounter("Hello World")
up, low = t.count()
print("Upper:", up)
print("Lower:", low)

print("\n=== PASCAL TRIANGLE ===")
p = PascalTriangle(5)
for row in p.generate():
    print(row)

print("\n=== KUADRAT LIST ===")
lst = ListSquarer([1, 2, 3, 4])
print(lst.square())
