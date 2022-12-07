class bio:
    def __init__(self, nama):
        self._nama = nama
        
class org1(bio):
    def __init__(self, nama, umur):
        super().__init__(nama)
        self._umur = umur
        
    def perkenalan(self):
        print (f'hai, nama saya {self._nama} umur saya {self._umur}')
        
adit = org1('adit', 16)
adit.perkenalan()
        