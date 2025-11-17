
# Input nilai koin yang akan dimasukkan ke dalam pocket
pocket = []
while True:
    try:
        k = int(input("Koin yang akan dimasukkan dalam pocket ? (Ketik '0' jika selesai): "))
        if k not in pocket:
            if k == 0:
                break
            pocket.append(k)
        else:
            print(f"Koin {k} sudah ada, ulangi lagi")
    except ValueError:
        print("Harus integer!")

print("Pocket = ", list(pocket))

# ========================== GREEDY ALGORITHM ==========================
def greedy(target):
    coins = sorted(pocket, reverse=True)  # Urutkan koin dari besar ke kecil
    hasil = []                            # Menyimpan kombinasi koin hasil greedy
    for koin in coins:                    # Coba setiap koin dari terbesar
        while target >= koin:             # Selama koin masih bisa diambil
            hasil.append(koin)            # Tambahkan ke hasil
            target -= koin                # Kurangi target dengan nilai koin
    return hasil                          # Kembalikan kombinasi akhir


# ========================== BRUTE FORCE ALGORITHM ==========================
def brute_force(target, start=0, current=None, hasils=None):
    if current is None:                   # List sementara untuk kombinasi saat ini
        current = []
    if hasils is None:                    # List utama untuk semua kombinasi valid
        hasils = []

    if target == 0:                       # Jika target tercapai, simpan kombinasi
        hasils.append(list(current))
        return hasils
    elif target < 0:                      # Jika target negatif, hentikan percabangan
        return hasils

    # Mencoba semua koin mulai dari indeks 'start' agar urutan tidak duplikat
    for i in range(start, len(pocket)):
        koin = pocket[i]                  # Ambil koin ke-i
        current.append(koin)              # Tambahkan ke kombinasi sementara
        brute_force(target - koin, i, current, hasils)  # Rekursi dengan target baru
        current.pop()                     # Hapus koin terakhir (backtrack)

    return hasils                         # Kembalikan semua kombinasi valid


# ========================== INPUT & OUTPUT ==========================
while True:                               # Ulangi sampai input berupa integer
    try:
        x = int(input("Target untuk dihabiskan = "))
        break
    except ValueError:
        print("Harus integer !")

# -------------------------- HASIL GREEDY --------------------------
greedy_result = greedy(x)
print("\nGreedy:", greedy_result)
print("Jumlah koin (Greedy):", len(greedy_result))

# -------------------------- HASIL BRUTE FORCE --------------------------
hasil = brute_force(x)
print("\nTotal kombinasi (Brute Force):", len(hasil))

# Menentukan kombinasi paling sedikit koin (optimal)
optimal_bruteForce = min(hasil, key=len)
print("Kombinasi optimal (Brute Force):", optimal_bruteForce)
print("Jumlah koin (Optimal Brute Force):", len(optimal_bruteForce))

# -------------------------- TAMPILKAN 20 KOMBINASI PERTAMA --------------------------
print("\n20 kombinasi pertama:")
for n, combination in enumerate(hasil[:20], 1):
    print(f"{n}. {combination}")
if len(hasil) > 20:
    print(f"Dan {len(hasil) - 20} kombinasi lainnya...")

