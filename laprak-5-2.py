#deret bilangan ganjil atas bawah 
def Ganjil(bilangan_1, bilangan_2):
    if bilangan_2 > bilangan_1:
        while bilangan_2 != bilangan_1:
            if bilangan_2 % 2 == 1:
                print(bilangan_2, end=",")
            bilangan_2 = bilangan_2 - 1
    else:
        while bilangan_2 != bilangan_1:
            bilangan_2 = bilangan_2 + 1
            if bilangan_2 %  2 == 1:
                print(bilangan_2, end=",")

nilai_bawah = int(input("Masukan nilai bawah : "))
nilai_atas =  int(input("Masukan nilai atas : "))
Ganjil(nilai_atas,nilai_bawah)
