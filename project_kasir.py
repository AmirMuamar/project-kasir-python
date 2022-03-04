#Project Simulation of a Supermarket


#array list data
huruf = ['A','B','C','D','E']
all_items = [ { "item": "susu", "harga": 50000 }, {"item": "daging", "harga": 20000} , {"item": "lampu", "harga": 15000} , {"item": "masker", "harga": 25000}, {"item": "apel", "harga": 30000} ]
promo = [ { "item": "susu", "harga" : 50000 }, {"item": "masker", "harga" : 25000} ]

#array penambahan data
totalHarga = []
barangDibeli = []
banyakBarang = []

#singkat script
h = "\n\n"
i = 40*"="
j = 30*"-"

#function tampilkan harga promo
def listHargaPromo() :
    print (i)
    for x in range(2):
        print (promo[x]["item"] + "\t= " + str(promo[x]["harga"]) + " (" + huruf[x] + ")")
    print (i)

#function tampilkan harga normal
def listhargaNormal() :
    print (i)
    for x in range(5):
        print (all_items[x]["item"] + "\t= " + str(all_items[x]["harga"]) + " (" + huruf[x] + ")")
    print (i)

#function input data pilihan barang dan jumlahnya
def hargaPromo(item,kode) :
    if kode == 1 :
        print ("Item\t= " + all_items[item]["item"])
    else :
        print ("Item\t= " + promo[item]["item"])
    banyak = int(input("Banyak\t= "))
    print(j)
    if kode == 1 :    
        jumlah = banyak * all_items[item]["harga"]
        print ("TOTAL" + "\t= " + str(all_items[item]["harga"]) + " x " +str(banyak)) 
    else :
        jumlah = banyak * promo[item]["harga"]
        print ("TOTAL" + "\t= " + str(promo[item]["harga"]) + " x " +str(banyak))
    totalHarga.append(jumlah)
    barangDibeli.append(item)
    banyakBarang.append(banyak)
    print ("\t= " + str(jumlah))
    print(j)

#function perhitungan dan tampilan akhir
def akhir(kode) :
    keseluruhan = sum(totalHarga)
    print(h)
    
    print("TOTAL HARGA\t: " + str(keseluruhan))
    print(j + "\nDetail:")
    for x in range (len(barangDibeli)) :
        if kode == 1 :    
            print (str(banyakBarang[x]) + "  " + all_items[barangDibeli[x]]["item"] +"\t-> Rp."+ str(totalHarga[x]))
        elif kode == 2 :
            print (str(banyakBarang[x]) + "  " + all_items[barangDibeli[x]]["item"] +"\t-> Rp."+ str(totalHarga[x]))
    
    totalHarga.clear()
    barangDibeli.clear()
    banyakBarang.clear()

#function jika salah
def jikaSalah() :
    print ("Pilihan anda salah. Silakan ulangi")
    print (40*"X")

#Program utama
b = True
while b:
    #pembukaan
    print(h)
    print (40*"*")
    print ("Selamat Datang di Supermarket")
    print (40*"*" + h)
    print ("Berikut Promo Item kami")
    listHargaPromo()
    print ("Pilih P : Promo Items \nPilih A : All Items")
    lainnya = input("(Pilih P/A)\t")

    print("\n\n")
    
    #Pilihan harga normal
    if lainnya == 'A' :
        listhargaNormal()
        kode = 1
        tambah ='Y'
        while tambah == 'Y' :
            pilih = input("pilih barang(A/B/C/D/E)\t")
            print(h+i)
            if pilih == 'A': 
                item = 0
                hargaPromo(item, kode)
            elif pilih == 'B' : 
                item = 1
                hargaPromo(item, kode)
            elif pilih == 'C' : 
                item = 2
                hargaPromo(item, kode)
            elif pilih == 'D' : 
                item = 3
                hargaPromo(item, kode)
            elif pilih == 'E' : 
                item = 4
                hargaPromo(item, kode)
            else :
                jikaSalah()
            tambah = input("Tambah barang? (Y/N)\t")
            print(i)
        akhir(kode)

    #Pilihan harga Promo
    elif lainnya == 'P' :
        listHargaPromo()
        kode = 2
        tambah = 'Y'
        while tambah == 'Y' :
            pilih = input("pilih barang(A/B)\t")
            print(h+i)
            if pilih == 'A':
                item = 0
                hargaPromo(item,kode)
            elif pilih == 'B':
                item = 1
                hargaPromo(item,kode)
            else : jikaSalah()
            tambah = input("Tambah barang?(Y/N)\t")
            print(i)
        akhir(kode)
    else : 
        jikaSalah()
    
    #penutup
    print(i+"\n"+i)
    keluar = input("Ulangi?(Y/N)\t")
    print(i+"\n\n\n")
    if keluar == 'N' :
        print ("TERIMA KASIH\n")
        b = False

