class agama:
    def __init__(self, nama, kepercayaan):
        self.nama = nama 
        self.kepercayaan = kepercayaan
        
    def perkenalan(self):
        print (self.nama,"beragama",self.kepercayaan)
    
        
        
class islam(agama):
    def __init__(self, nama, kepercayaan, sholat):
        agama.__init__(self, nama, kepercayaan)
        self.sholat = sholat
        
class kristen(agama):
    def __init__(self, nama, kepercayaan, sembahyang):
        agama.__init__(self, nama, kepercayaan)
        self.sembahyang = sembahyang
        
        
    
hisyam = islam('hisyam','islam','sholat')
hisyam.perkenalan()
print (f'{hisyam.nama} beribadah dengan melakukan {hisyam.sholat}\n')

abraham = kristen('abraham', 'kristen', 'sembahyang')
abraham.perkenalan()
print (f'{abraham.nama} beribadah dengan melakukan {abraham.sembahyang}\n')


                
