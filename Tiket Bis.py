surabaya = 300000
bali = 350000
lampung = 500000

print("Pilihan")
print("Surabaya : 300K")
print("Bali     : 350K")
print("Lampung  : 500K")
print()

nama = str(input("Masukkan nama anda          : ")).capitalize()
no = input("Masukkan no handphone anda  : ")
jurusan = input("Pilih jurusan               : ").capitalize()
jumlah = int(input("Masukkan jumlah tiket       : "))

if jurusan == "Surabaya":
    total = surabaya * jumlah
elif jurusan == "Bali":
    total = bali * jumlah
elif jurusan == "Lampung":
    total = lampung * jumlah
else:
    total = 0

diskon = total * 0.1
if jumlah >= 3:
    print("Anda mendapatkan diskon 10%")
    total -= diskon
else:
    diskon = 0

print()
print("=============== Struk Pembelian Tiket ===============")
print("Nama     : ", nama)
print("Nomor HP : ", no)
print("Jurusan  : ", jurusan)
print("Jumlah   : ", jumlah)
print("Harga    : ", int(total))
print("=====================================================")
