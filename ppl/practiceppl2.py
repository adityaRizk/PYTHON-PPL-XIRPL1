# contoh operator overloading penambahan
print ('contoh penambahan')

class Angka:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self, objek):
        return Angka(
        self.angka + objek.angka
        )
    
x1 = Angka(7)
x2 = Angka(9)
x3 = x1 + x2

print(x3.angka)

# contoh operator overloading pengurangan
print ('contoh pengurangan')
class Angka2:
    def __init__(self, angka2):
        self.angka2 = angka2

    def __sub__(self, objek):
        return Angka2(
        self.angka2 - objek.angka2
        )
    
x1 = Angka2(30)
x2 = Angka2(19)
x3 = x1 - x2

print(x3.angka2)