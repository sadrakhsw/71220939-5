x = int(input("Berapa jumlah mata kuliah ? "))
print()
jumlah_mata_kuliah = 0
for y in range(0,x):
        temp = input("Nilai MK %d: " % (y + 1))
        if temp == "A" :
            skor = 4
        elif temp == "B" :
            skor = 3
        elif temp == "C" :
            skor = 2
        elif temp == "D" :
            skor = 1
        jumlah_mata_kuliah += skor
rata_rata = jumlah_mata_kuliah / x 

print("\nRata-rata = %0.2f" % rata_rata)
