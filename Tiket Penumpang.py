# Inisialisasi list penumpang
penumpang = []

# Fungsi untuk menambahkan penumpang
def tambah_penumpang():
    jumlah = int(input("Masukkan jumlah penumpang yang akan ditambahkan: "))
    for _ in range(jumlah):
        nama = input("Masukkan nama penumpang: ")
        if not nama.isalpha():  # Memastikan nama hanya berisi huruf
            print("Nama penumpang hanya boleh berisi huruf.")
        else:
            nama = nama.capitalize()  # Mengubah nama menjadi huruf kapital
            if nama in penumpang:
                print(f"{nama} sudah ada dalam daftar penumpang.")
            else:
                penumpang.append(nama)
                print(f"{nama} berhasil ditambahkan ke dalam daftar penumpang.")

# Fungsi untuk penumpang turun
# Fungsi untuk penumpang turun
# Fungsi untuk penumpang turun
def penumpang_turun():
    jumlah = int(input("Masukkan jumlah penumpang yang akan turun: "))
    penumpang_terturunkan = 0
    
    for _ in range(jumlah):
        while True:
            nama = input("Masukkan nama penumpang yang turun: ")
            if not nama.isalpha():  # Memastikan nama hanya berisi huruf
                print("Nama penumpang hanya boleh berisi huruf.")
            else:
                nama = nama.capitalize()  # Mengubah nama menjadi huruf kapital
                if nama in penumpang:
                    penumpang.remove(nama)
                    penumpang_terturunkan += 1
                    print(f"{nama} telah turun dari angkutan.")
                    break  # Keluar dari loop saat nama yang valid ditemukan
                else:
                    print(f"{nama} tidak ada dalam daftar penumpang. Coba lagi.")

    if penumpang_terturunkan < jumlah:
        print(f"{jumlah - penumpang_terturunkan} penumpang tidak ditemukan dalam daftar penumpang.")


# Fungsi untuk mencetak daftar penumpang dalam format nota
def cetak_daftar_penumpang():
    print("")
    print("========== Nota Angkutan ==========")
    print("No. | Nama Penumpang")
    print("-------------------------------")
    for i, nama in enumerate(penumpang, start=1):
        print(f"{i}.  | {nama}")
    print("-------------------------------")
    print(f"Total Penumpang: {len(penumpang)}")
    print("===================================")

# Loop utama aplikasi
while True:
    print("\nMenu:")
    print("1. Tambah Penumpang")
    print("2. Penumpang Turun")
    print("3. Cetak Daftar Penumpang")
    print("4. Keluar")
    print("")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        tambah_penumpang()
    elif pilihan == '2':
        penumpang_turun()
    elif pilihan == '3':
        cetak_daftar_penumpang()
    elif pilihan == '4':
        print("Terima kasih atas kepercayaan Anda menggunakan Layanan Angkutan Kami. Semoga perjalanan Anda menyenangkan!")
        print("")
        break
    else:
        print("Menu tidak valid. Silakan pilih menu yang sesuai.")
