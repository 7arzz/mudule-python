# Operasi Aritmatika

a = 10
b = 3

hasil = a + b
print("a + b = ",hasil)

hasil = a - b
print("a - b = ",hasil)

hasil = a * b
print("a * b = ",hasil)

hasil = a / b
print("a / b = ",hasil)   

hasil = a % b
print("a % b = ",hasil)

hasil = a ** b
print("a ** b = ",hasil) 

hasil = a // b
print("a // b = ",hasil)


# Prioritas Operasi

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print("x ** y * z + x / y - y % z // x = ",hasil)

# prioritas kurung
hasil1 = x ** y * (z + x) / y - y % z // x
print("x ** y * (z + x) / y - y % z // x = ",hasil1)

# Operasi Komparasi
#  tiap hasil operasi komparasi adalah boolean
# >, <, >==, <==, ==, !=, is, is not

a = 4
b = 2

#  > lebih besar
hasil = a > b
print ("a > b = ",hasil)

#   < lebih kecil
hasil1 = a < b
print ("a < b = ",hasil1)

#   >= lebih besar sama dengan
hasil2 = a >= b
print ("a >= b = ",hasil2)

#   <= lebih kecil sama dengan
hasil3 = a <= b
print ("a <= b = ",hasil3)

#   == sama dengan
hasil4 = a == b
print ("a == b = ",hasil4)

#   != tidak sama dengan
hasil5 = a != b
print ("a != b = ",hasil5)


# is sebagai komparasi objek identity
x = 5 # ini adalah assignment membuat object
y = 5

print('nilai x = ', x, 'id = ', hex(id(x)))
print('nilai y = ', y, 'id = ', hex(id(y)))

hasil6 = x is y
print('x is y = ', hasil6)

hasil7 = x is not y
print('x is not y = ', hasil7)


#  opertator yang dilakukan dg penyingkatan


a = 5 # adalah assignment
print ("nilai a = ", a)

a = a + 1
print ("nilai a += 1 = ", a)

a += 1
print ("nilai a += 1 = ", a, "\n Maka nilai a sekarang = ", a)

a -= 2
print ("nilai a -= 1 = ", a, "\n Maka nilai a sekarang = ", a)

a *= 2
print ("nilai a *= 2 = ", a, "\n Maka nilai a sekarang = ", a)

a /= 2
print ("nilai a /= 2 = ", a, "\n Maka nilai a sekarang = ", a)

a **= 2
print ("nilai a **= 2 = ", a, "\n Maka nilai a sekarang = ", a)

a %= 2
print ("nilai a %= 2 = ", a, "\n Maka nilai a sekarang = ", a)



b = 10
print ("\n nilai b = ", b)

b %= 3
print ("nilai b %= 3 = ", b, "\n Maka nilai b sekarang = ", b)

b //= 2
print ("nilai b //= 2 = ", b, "\n Maka nilai b sekarang = ", b)

a = 5
print ("\n nilai a = ", a)
a **= 3
print ("nilai a **= 3 = ", b, "\n Maka nilai a sekarang = ", b)


# Operasi Bitwise

# OR
c = True
print ("\n nilai c = ", c)
c  |= False
print ("nilai c |= False = ", c, "\n Maka nilai c sekarang = ", c)

c = False
print ("\n nilai c = ", c)
c  |= False
print ("nilai c |= True = ", c, "\n Maka nilai c sekarang = ", c)

# AND
c = True
print ("\n nilai c = ", c)
c  &= False
print ("nilai c &= False = ", c, "\n Maka nilai c sekarang = ", c)

c = True
print ("\n nilai c = ", c)
c  &= True
print ("nilai c &= True = ", c, "\n Maka nilai c sekarang = ", c)

# XOR
c = True
print ("\n nilai c = ", c)
c  ^= False
print ("nilai c ^= False = ", c, "\n Maka nilai c sekarang = ", c)

c = True
print ("\n nilai c = ", c)
c  ^= True
print ("nilai c ^= True = ", c, "\n Maka nilai c sekarang = ", c)

# Geser Geser
d = 0b0100
print ("\n nilai d = ", format(d, '04b'))
d >>= 2
print ("nilai d >>= 2 = ", format(d, '04b'), "\n Maka nilai d sekarang = ", format(d, '04b'))

d <<= 1
print ("nilai d <<= 2 = ", format(d, '04b'), "\n Maka nilai d sekarang = ", format(d, '04b'))

# =====================================================
# Operasi logika
# and, or, not
# =====================================================

# NOT
print("===== NOT =====")
a = False
c = not a
print ('data a = ', a)
print('================= NOT ')
print('data c = ', c)

# OR
print("===== OR =====")

a = False
b = False
c = a or b
print (a , 'OR' ,b, '=', c)

a = False
b = True
c = a or b
print (a , 'OR' ,b, '=', c)

a = True
b = False
c = a or b
print (a , 'OR' ,b, '=', c)

a = True
b = True
c = a or b
print (a , 'OR' ,b, '=', c)


# AND
print("===== AND =====")

a = False
b = False
c = a and b
print (a , 'AND' ,b, '=', c)

a = False
b = True
c = a and b
print (a , 'AND' ,b, '=', c)

a = True
b = False
c = a and b
print (a , 'AND' ,b, '=', c)

a = True
b = True
c = a and b
print (a , 'AND' ,b, '=', c)


# XOR
print("===== XOR =====")

a = False
b = False
c = a ^ b
print (a , 'XOR' ,b, '=', c)

a = False
b = True
c = a ^ b
print (a , 'XOR' ,b, '=', c)

a = True
b = False
c = a ^ b
print (a , 'XOR' ,b, '=', c)

a = True
b = True
c = a ^ b
print (a , 'XOR' ,b, '=', c)

# =====================================================
# operator bitwise, operator biner, binary
# =====================================================

a = 9
b = 5 

#OR (    |   )
c = a | b
print ('\n==== OR =====')
print ('nilai : ', a, 'Binary : ' , format(a, '08b'))
print ('nilai : ', b, 'Binary : ' , format(b, '08b'))
print ("_____________________________________ ( | )")
print ('nilai : ', c, 'Binary : ' , format(c, '08b'))


# AND ( & )
c = a & b
print ('\n==== AND =====')
print ('nilai : ', a, 'Binary : ' , format(a, '08b'))
print ('nilai : ', b, 'Binary : ' , format(b, '08b'))
print ("_____________________________________ ( & )")
print ('nilai : ', c, 'Binary : ' , format(c, '08b'))

# XOR (  ^   )
c = a ^ b
print ('\n==== XOR =====')
print ('nilai : ', a, 'Binary : ' , format(a, '08b'))
print ('nilai : ', b, 'Binary : ' , format(b, '08b'))
print ("_____________________________________ ( ^ )")
print ('nilai : ', c, 'Binary : ' , format(c, '08b'))

# NOT ( ~ )
c = ~a
print ('\n==== NOT =====')
print ('nilai : ', a, 'Binary : ' , format(a, '08b'))
print ("_____________________________________ ( ~ )")
print ('nilai : ', c, 'Binary : ' , format(c, '08b'))


# Shift Right ( >>  )
c = a >> 1
print ("\n==== >> =====")
print('nilai : ', a , 'Binary : ' , format(a,'08b'))
print ("_____________________________________ ( >> )")
print ('nilai : ', c, 'Binary : ' , format(c, '08b'))

# Shift Left ( <<  )
c = a << 2
print ("\n==== << =====")
print('nilai : ', a , 'Binary : ' , format(a,'08b'))
print ("_____________________________________ ( << )")
print ('nilai : ', c, 'Binary : ' , format(c, '08b'))

# =====================================================
# Operator Identitas (Identity Operators)
# is dan is not
# =====================================================

print("\n===== Operator Identitas (is, is not) =====")

a = 10
b = 10
c = [1, 2, 3]
d = [1, 2, 3]

# Cek nilai dan id object
print("nilai a =", a, "| id =", hex(id(a)))
print("nilai b =", b, "| id =", hex(id(b)))

print("nilai c =", c, "| id =", hex(id(c)))
print("nilai d =", d, "| id =", hex(id(d)))

# is → True jika objeknya sama di memori
print("\na is b =", a is b)     # biasanya True (object caching)
print("c is d =", c is d)      # False (list beda object)

# is not → kebalikan is
print("\na is not b =", a is not b)
print("c is not d =", c is not d)


# =====================================================
# Urutan Prioritas Operator
# =====================================================
print("\n===== Urutan Prioritas Operator =====")

print("""
1.  ()          → Kurung (dieksekusi paling awal)
2.  **          → Pangkat
3.  +x, -x, ~x  → Unary (tanda +/-, NOT bitwise)
4.  *, /, //, % → Perkalian, pembagian, floor division, modulus
5.  +, -        → Penjumlahan, pengurangan
6.  <<, >>      → Shift kiri/kanan
7.  &           → Bitwise AND
8.  ^           → Bitwise XOR
9.  |           → Bitwise OR
10. ==, !=, >, <, >=, <=, is, is not, in, not in
11. not         → Logika NOT
12. and         → Logika AND
13. or          → Logika OR
""")

# Contoh penerapan
print("===== Contoh Pengaruh Prioritas =====")

hasil = 3 + 4 * 2
print("3 + 4 * 2 =", hasil)   # 4*2 dulu = 8 → 3+8 = 11

hasil = (3 + 4) * 2
print("(3 + 4) * 2 =", hasil) # kurung dulu → 7*2 = 14

hasil = 5 + 2 ** 3 * 2
print("5 + 2 ** 3 * 2 =", hasil)  # 2**3 = 8 → 8*2 = 16 → +5 = 21

hasil = 10 > 5 and 3 < 1
print("10 > 5 and 3 < 1 =", hasil)  # True and False → False

hasil = not 5 == 5
print("not 5 == 5 =", hasil)  # 5==5 True → not True = False


# ======================================================
# Latihan Module 4
# ======================================================


# PROGRAM 1: Perhitungan Sederhana


BilanganPertama = 15
BilanganKedua = 8
BilanganKetiga = 100

RumusPengjumlahan = BilanganPertama + BilanganKedua + BilanganKetiga
RumusPengurangan = BilanganPertama - BilanganKedua - BilanganKetiga
RumusPerkalian = BilanganPertama * BilanganKedua * BilanganKetiga

print("Pengjumlahan = 15 + 8 + 100 =", RumusPengjumlahan)
print("Pengurangan = 15 - 8 - 100 =", RumusPengurangan)
print("Perkalian = 15 x 8 x 100 =", RumusPerkalian)

# PROGRAM 2: Luas Bangun Datar


# 1. Luas Persegi
panjang_sisi = 20
luas_persegi = panjang_sisi * panjang_sisi

# 2. Luas Persegi Panjang
panjang_pp = 50
lebar_pp = 25.5
luas_pp = panjang_pp * lebar_pp

# 3. Luas Segitiga
alas_segitiga = 40
tinggi_segitiga = 60
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga

# 4. Luas Lingkaran
phi = 3.14
r = 15
luas_lingkaran = phi * r * r

# 5. Luas Jajaran Genjang
alas_jg = 30
tinggi_jg = 25
luas_jg = alas_jg * tinggi_jg

# 6. Luas Trapesium
a = 40
b = 20
tinggi_tp = 35
luas_trapesium = 0.5 * (a + b) * tinggi_tp

print("Luas Persegi =", luas_persegi)
print("Luas Persegi Panjang =", luas_pp)
print("Luas Segitiga =", luas_segitiga)
print("Luas Lingkaran =", luas_lingkaran)
print("Luas Jajaran Genjang =", luas_jg)
print("Luas Trapesium =", luas_trapesium)


# PROGRAM 3: Operator Bitwise

a = 9
b = 5

print("a & b =", a & b)
print("a | b =", a | b)
print("~a =", ~a)
print("a ^ b =", a ^ b)
