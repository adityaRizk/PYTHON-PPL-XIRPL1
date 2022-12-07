#latihan overloading

class angka:
    def __init__(self, angka):
        self.angka = angka
        
    def __add__(self, object):
        return self.angka + object.angka
        
        
x1 = angka(20)
x2 = angka(30)
x1 + x2

print(x1+ x2)