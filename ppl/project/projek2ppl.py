#menu untuk tampilan perpus



#perpus kosng ntuk menyimpan buku
def line():
    print("O=============================O")
def line2():
    print("O-----------------------------O")
    
    
buku = []

#fungsi show buku
def show_buku():
    if len(buku) <= 0:
        print("no ada book")
        line()
    else:
        for index in range(len(buku)):
            print("[{}] {}".format (index,buku [index]))
            line()

#fungsi untuk edit buku
def edit_buku():
    indeks = int(input("masukan id buku : "))
    if indeks > len(buku):
        print ("ID salah")
        line2()
    else:
        judul_baru = input("masukan judul baru : ")
        buku[indeks] = judul_baru
        line2()
        print("buku berhasil dirubah")
        show_buku()
        line()

#fungsi insert buku
def insert_buku():
    line()
    buku_baru = input("judul buku : ")
    buku.append(buku_baru)
    line()
    line2()
    print("buku berhasil ditambahkan")
    line2()
#fungsi delet
def delet_buku():
    show_buku()
    indeks = int(input("maskan id buku : "))
    if indeks > len(buku):
        print ("ID salah")
    else:
        buku.remove(buku[indeks])
        line()
        print ("buku berhasil dihapus!!!!!!!!!!!!!!!!!!")
        line2()

#menu untuk tampilan perpus

def show_menu():
    print("\n")
    print("welcome to perpus--")
    print("1.show buku")
    print("2.insert buku")
    print("3.edit buku")
    print("4.delet buku")
    print("5.exit")
    
    menu = int(input("pilih menu : >"))

    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delet_buku()
    elif menu == 5:
        exit()
    else:
        print("salah pilih")

#tampilkan menu
show_menu()


#tampilkan menu
if __name__ == "__main__":
    while True:
        show_menu()