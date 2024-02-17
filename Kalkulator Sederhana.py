def hitung_faktorial(n):
    faktorial = 1 # 1 x 1 = y,  y x 2 = y2, y2 x 3 : faktorial dari 3

    for i in range(1, n + 1): #(1,) =  mulai dari satu, (,n + 1) = dia berhenti di n + 1
        faktorial *= i # *= : kali sama dengan
    return faktorial

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

while True:
    print("")
    print("Kalkulator Sederhana")
    print("1. Hitung Faktorial (!)")
    print("2. Penjumlahan (+)")
    print("3. Pengurangan (-)")
    print("4. Keluar")
    
    pilihan = input("Pilih operasi (1/2/3/4): ")
    
    if pilihan == '1':
        angka = int(input("Masukkan angka untuk menghitung faktorial: "))
        hasil = hitung_faktorial(angka)
        print(f"Hasil faktorial dari {angka} adalah {hasil}") #Pada baris ini, f-string digunakan untuk memasukkan nilai variabel hasil ke dalam string yang akan dicetak. Ketika kode dijalankan, nilai dari variabel hasil akan diambil dan dimasukkan ke dalam posisi {hasil} dalam string tersebut. Ini memungkinkan Anda untuk mencetak nilai variabel dengan mudah tanpa harus melakukan konversi manual atau penggabungan string.

    elif pilihan == '2':
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        hasil = penjumlahan(a, b)
        print(f"Hasil penjumlahan: {hasil}")

    elif pilihan == '3':
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        hasil = pengurangan(a, b)
        print(f"Hasil pengurangan: {hasil}")

    elif pilihan == '4':
        print("Bye!")
        print("")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.")
