a = 10
b = 3

#operasi aritmatika penambahan
hasil = a + b
print(a, "+", b, "=", hasil)

#operasi aritmatika pengurangan
hasil = a - b
print(a, "-", b, "=", hasil)

#operasi aritmatika perkalian
hasil = a * b
print(a, "*", b, "=", hasil)

#operasi aritmatika pembagian
hasil = a / b
print(a, ":", b, "=", hasil)

#operasi aritmatika pangkat (eksponen)
hasil = a ** b
print(a, "**", b, "=", hasil)

#operasi atimatika modulus(%) sisa hasil pembagian
hasil = a % b
print(a, "%", b, "=", hasil)

#operasi aritmatika floor division //
hasil = a // b
print(a, "//", b, "=", hasil)

#prioritas operasi/ operational precedence (), eksponen, perkalian, pertambahan
x = 4
y = 5
z = 6

hasil = x // y ** z - x * z % z + x / y
print("hasilnya adalah", hasil)