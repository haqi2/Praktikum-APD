namabarang = str(input ("masukkan nama barang "))
hargabarang = float(input("masukkan harga barang "))
jumlahbarang = int(input("masukkan jumlah barang "))
diskon = float(input("masukkan diskon "))
totalbarang = hargabarang * jumlahbarang
totaldiskon = totalbarang * 0.81
totalharga = totalbarang - totaldiskon
mod = diskon%3
print ("Kamu membeli", jumlahbarang, namabarang,"dengan harga satuan", hargabarang, "harga sebelum diskon", totalbarang, "total diskon adalah", totalharga )
print (diskon, "dibagi 3 sisanya", mod )
