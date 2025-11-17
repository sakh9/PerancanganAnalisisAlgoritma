# Fungsi mencari nilai max dari list dengan metode brute force
def bruteForceMax(inputList):

    if not inputList:                               # Mengecek apakah list kosong
        raise ValueError("List gaboleh kosong.")

    maxValue = inputList[0]                         # Isi nilai maksimum dengan elemen pertama
    for item in inputList:                          # Looping melalui setiap elemen dalam list
        if item > maxValue:                         # Jika elemen saat ini lebih besar dari nilai maksimum saat ini
            maxValue = item                         # Maka update nilai maksimum menjadi elemen saat ini

    return f"Nilai maksimum dari list {inputList} \n ialah {maxValue}"


print("Minimal 5 dan Maksimal 10 angka untuk mencari nilai maksimum")

# Mengambil input dari user
listOfNumbers = []

while len(listOfNumbers) < 5 or len(listOfNumbers) < 10:        # Ketika jumlah elemen kurang dari 5 atau kurang dari 10
    while True:
        try:
            if len(listOfNumbers) == 10:                        # Jika jumlah elemen sudah 10, maka keluar dari loop
                break
            userInput = input(f"Masukkan angka (input 'z' jika selesai) {listOfNumbers}\n= ")   # Mengambil input dari user

            if userInput.lower() == "z":                        
                break

            x = int(userInput)                    
            listOfNumbers.append(x)

        except ValueError:
            print("Harus integer !")

    if userInput.lower() == "z":
        if len(listOfNumbers) < 5:
            print("Harus minimal 5 angka !")
        else:
            break

print(bruteForceMax(listOfNumbers))




