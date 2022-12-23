print("----------------- SELAMAT DATANG DI KEDAI RADEN -----------------")
nama = input("MASUKKAN NAMA ANDA : ")
Alamat = input("MASUKKAN ALAMAT : ")
No_telp = input("MASUKKAN NO TELP ")

#buat waktu
import time
tanggal = time.strftime("%D-%M ,%H:%M:%S")
print(tanggal)

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Belatung bakar - Rp 1000000")
   print("2. Laron pepes - Rp 2000000")
   print("3. Oseng oseng kucing - Rp 3000000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))

   if nomor==1:
       totalmkn=porsi*1000000
       print (porsi," Porsi Belatung bakar = Rp", totalmkn)
       mkn=("Belatung bakar")
   elif nomor==2:
       totalmkn=porsi*2000000
       print (porsi," Porsi Laron pepes = Rp", totalmkn)
       mkn=("Laron pepes")
   elif nomor==3:
       totalmkn=porsi*3000000
       print (porsi, " Porsi Oseng oseng kucing = Rp", totalmkn)
       mkn=("Oseng oseng kucing")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es Gedebong pisang  - Rp 50000")
   print("2. Es Mogi mogi - Rp 100000")
   print("3. Es Kacang masih ada tanahnya - Rp 150000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*50000
       print (gelas," Gelas Es Gedebong pisang = Rp", totalmnm)
       mnm=("Es Gedebong pisang")
   elif nomor==2:
       totalmnm=gelas*100000
       print (gelas, " Gelas Es Mogi mogi = Rp", totalmnm)
       mnm=("Es Mogi mogi")
   elif nomor==3:
       totalmnm=gelas*150000
       print (gelas, " Gelas Es Kacang masih ada tanahnya = Rp", totalmnm)
       mnm=("es Kacang masih ada tanahnya")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== STRUK PEMBELIAN =========")
print("==================================")
print ("Nama\t\t:",nama)
print ("Alamat\t\t:",Alamat)
print ("No telp\t\t:",No_telp)
print ("Tanggal\t\t:",tanggal)

print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")