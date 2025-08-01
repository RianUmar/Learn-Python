#Operasi aritmatika

a = 10
b = 3

# Penjumlahan
hasil_penjumlahan = a + b
print(a, "+", b, "=", hasil_penjumlahan)

# Pengurangan
hasil_pengurangan = a - b
print(a, "-", b, "=", hasil_pengurangan)

# Perkalian
hasil_perkalian = a * b
print(a, "x", b, "=", hasil_perkalian)

# Pembagian
hasil_pembagian = a / b
print(a, "/", b, "=", hasil_pembagian)

# Modulus
hasil_modulus = a % b
print(a, "%", b, "=", hasil_modulus)

# Eksponen (pangkat)
hasil_eksponen = a ** b
print(a, "^", b, "=", hasil_eksponen)

# Floor Division (pembagian bulat)
hasil_floor_division = a // b
print(a, "//", b, "=", hasil_floor_division)

# Prioritas operasi, operational precedence
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print("Hasil dari operasi kompleks:", hasil) 

'''
  1. ()
  2. Exponen **
  3. Perkalian dan teman teman * / // ** %
  4. Penjumlahan dan pengurangan + -
'''