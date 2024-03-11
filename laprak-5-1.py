def perkalian(angka_pertama,angka_kedua):
    for x in range (angka_pertama):
        if x == angka_pertama - 1:
            print(angka_kedua, end="=")
        else:
            print(angka_kedua, end="+")
    hasil = angka_pertama * angka_kedua
    return hasil

print(perkalian(6,5))
print(perkalian(7,10))
