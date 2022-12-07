class siswa:
    def __init__(self, nama):
        self.nama = nama

perkenalan = siswa('euroski')
print(f'1. siswa kami bernama {perkenalan.nama}')

class guru:
    def __init__(self, nama):
        self._nama = nama
        
class gurujp(guru):
    def __init__(self, nama):
        super().__init__(nama)
        self._nama = nama
    
    def kenalan(self):
        print(f'2. guru kami bernama {self._nama}')
        
ajar = gurujp('bu anita')
ajar.kenalan()


class kepsek:
    def __init__(self, nama):
        self.__nama = nama
    
    def tampilkan_nama(self):
        print(f'3. kepsek kami bernama {self.__nama}')
        
kepse = kepsek('pak Lilik')
kepse.tampilkan_nama()
