def cek_tahun_kabisat(tahun):
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

while True:
    print("\nKalkulator Tahun Kabisat")
    print("1. Masuk")
    print("2. Keluar\n")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == '1':

        try:
         tahun = int(input("Masukkan tahun : "))
       
         if cek_tahun_kabisat(tahun):
            print(f"{tahun} adalah tahun kabisat.")
         else:
            print(f"{tahun} bukan tahun kabisat.")
        except ValueError:
         print("Masukkan tahun yang valid (angka)!")
    elif pilihan == '2':
        print("Terima Kasih!\n")
        break
    else:
        print("Menu tidak valid. Silakan pilih menu yang sesuai.")
