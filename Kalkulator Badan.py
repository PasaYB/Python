def hitung_berat_badan_ideal(tinggi_cm, jenis_kelamin):
    if jenis_kelamin.lower() == "pria":
        berat_badan_ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.1)
    elif jenis_kelamin.lower() == "wanita":
        berat_badan_ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.15)
    else:
        berat_badan_ideal = None
    return berat_badan_ideal

while True:
    print("\nKalkulator Badan Ideal")
    print("1. Masuk")
    print("2. Keluar\n")

    pilihan = input("Pilih menu (1/2): ")

    if pilihan == '1':
        try:
         tinggi_cm = float(input("Masukkan tinggi Anda (cm): "))
         jenis_kelamin = input("Jenis kelamin Anda (pria/wanita): ")
        
         berat_badan_ideal = hitung_berat_badan_ideal(tinggi_cm, jenis_kelamin)
        
         if berat_badan_ideal is not None and berat_badan_ideal > 0:
            print(f"\nBerat badan ideal Anda adalah {berat_badan_ideal:.2f} kg")
         else:
            print("Masukkan jenis kelamin yang valid (pria/wanita).")
        except ValueError:
         print("Masukkan tinggi yang valid (angka).")

    elif pilihan == '2':
        print("Terima Kasih!\n")
        break
    else:
        print("Menu tidak valid. Silakan pilih menu yang sesuai.")