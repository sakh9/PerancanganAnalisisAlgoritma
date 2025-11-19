dataMHS = {}

# Input user
while True:
    nama = input("Masukkan nama siswa (ketik '0' untuk berhenti): ").strip()

    if not nama:                                        # Mengecek nama tdk boleh kosong
        print("Nama mahasiswa tidak boleh kosong.")
        continue

    if nama == '0':
        if not dataMHS:                                 # Mengecek data tdk boleh kosong
            print("Data mahasiswa tidak boleh kosong.")
            continue
        break

    if any(char.isdigit() for char in nama):            # Mengecek nama tidak boleh mengandung nomor
        print("Nama mahasiswa tidak boleh mengandung angka.")
        continue

    # Input IPK
    while True:
        s = input(f"Masukkan IPK untuk {nama} menggunakan '.' : ").replace(',', '.').strip()        # Mengganti (,) menjadi (.) 

        if not s:
            print("Input IPK tidak boleh kosong.")      # Mengecek input ipk tdk boleh kosong
            continue

        try:
            ipk = float(s)

        except ValueError:
            print("IPK tidak valid. Gunakan angka dengan titik desimal.")
            continue

        if not 0 <= ipk <= 4:
            print("IPK harus antara 0.0 hingga 4.0.")
            continue

        dataMHS[nama] = ipk
        break


# Fungsi rata rata
def rataRata(dataDict):
    if not dataDict:
        raise ValueError("Data mahasiswa kosong.")
    
    return sum(dataDict.values()) / len(dataDict)


# Fungsi nilai maksimum Brute force
def ipkMaksimum(dataDict):

    if not dataDict:
        raise ValueError("Data mahasiswa kosong.")
    
    maxNama = None
    maxIpk = float('-inf')                  # Ambil nilai paling kecil
    for nama, ipk in dataDict.items():      # Ambil nama dan ipk dari dictionary
        if ipk > maxIpk:
            maxIpk = ipk
            maxNama = nama
    
    return maxNama, maxIpk
    

# Fungsi nilai minimum Brute force
def ipkMinimum(dataDict):

    if not dataDict:
        raise ValueError("Data mahasiswa kosong.")
    
    minNama = None
    minIpk = float('inf')                 # Ambil nilai paling besar
    for nama, ipk in dataDict.items():
        if ipk < minIpk:
            minIpk = ipk
            minNama = nama
    
    return minNama, minIpk

# Menampilkan hasil
try:
    if not dataMHS:
        raise ValueError("Tidak ada data mahasiswa yang dimasukkan.")

    # TABEL HASIL
    print("\nDaftar IPK Mahasiswa")
    print("=" * 35)
    print(f"{'No':<5} {'Nama':<20} {'IPK':<5}")
    print("-" * 35)

    for i, (nama, ipk) in enumerate(dataMHS.items(), start=1):
        print(f"{i:<5}{nama:<20}{ipk:<5.2f}")

    print("=" * 35)

    print(f"Rata rata IPK mahasiswa: {rataRata(dataMHS):.2f}\n")

    namaMaks, ipkMaks = ipkMaksimum(dataMHS)
    print(f"Mahasiswa dengan IPK tertinggi: {namaMaks} dengan IPK {ipkMaks}\n")

    namaMin, ipkMin = ipkMinimum(dataMHS)
    print(f"Mahasiswa dengan IPK terendah: {namaMin} dengan IPK {ipkMin}")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
