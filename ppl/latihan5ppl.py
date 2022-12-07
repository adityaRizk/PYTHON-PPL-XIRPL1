#buat 3 object orang, pelajar, pekerja
#orang kelas induk
#pelajar , pekerja = kelas turunan

class orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal
        print("fungsi init dieksekusi")
        
                
    def perkenalan(self):
            print ("halo saya ",self.nama,"dari",self.asal)
            
            
class pelajar(orang):
    def __init__(self, nama, asal, sekolah):
        orang.__init__(self, nama, asal)
        self.sekolah = sekolah
        
class pekerja(orang):
    def __init__(self, nama, asal, kantor):
        super().__init__(nama, asal)
        self.kantor = kantor
            
andi = orang("Andi", "jkt\n")
andi.perkenalan()

titi = pelajar("titi", "subang", "smk")
titi.perkenalan()
print(f"saya sekolah di {titi.sekolah} \n")

jeponk = pekerja("jeponk", "planet bekasi", "jp")
jeponk.perkenalan()
print(f"saya kerja di {jeponk.kantor} \n")
