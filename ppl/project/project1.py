#fungsi garis
def garis():
    print ("===============================================")

# SELAMAT DATANG DI JPHOTEL
garis()
print("--Selamat Datang DI JPHOTEL--")
print("--NO----TIPE--------HARGA--")
print("--01----Suite---1.000.000--")
print("--02----Royal-----500.000--")
print("--03----BPJS------250.000--")

# Sampe Resepsionis (input data)
garis()
cust = input("Masukan nama lengkap : ")
tipe = int(input("Tipe Kamar : "))
lama_inap = int(input("Masukan lama inap : "))

# tipe kamar
garis()
if tipe == 1:
    tipe_kamar=("suite")
elif tipe == 2:
    tipe_kamar=("royal")
elif tipe == 3:
    tipe_kamar=("bpjs")
    
#kalkulasi harga total
if tipe == 1:
    total_harga = 1000000 * lama_inap
elif tipe == 2:
    total_harga = 500000 * lama_inap
elif tipe == 3:
    total_harga = 250000 * lama_inap
    
    
# struk JPHOTEL

print("Pelanggan atas nama : ", cust)
print("Tipe kamar yang dipilih :", tipe_kamar)
print("Lama menginap : ", lama_inap)
garis()
print("Total : ", "RP", total_harga, ",00")
