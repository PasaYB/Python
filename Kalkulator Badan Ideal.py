def hitung_berat_badan_ideal(tinggi_cm, jenis_kelamin):
    if jenis_kelamin.lower() == "pria":
        berat_badan_ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.1)
    elif jenis_kelamin.lower() == "wanita":
        berat_badan_ideal = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.15)
    else:
        berat_badan_ideal = None
    return berat_badan_ideal

while True:
    try:
        tinggi_cm = float(input("Masukkan tinggi Anda (cm): "))
        jenis_kelamin = input("Jenis kelamin Anda (pria/wanita): ")
        
        berat_badan_ideal = hitung_berat_badan_ideal(tinggi_cm, jenis_kelamin)
        
        if berat_badan_ideal is not None:
            print(f"Berat badan ideal Anda adalah {berat_badan_ideal:.2f} kg.")
        else:
            print("Masukkan tinggi dan jenis kelamin yang valid.")
    except ValueError:
        print("Masukkan tinggi yang valid (angka) atau jenis kelamin yang valid (pria/wanita).")
