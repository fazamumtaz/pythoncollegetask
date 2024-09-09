# Masukkan angka yang ingin kita test
angka1 = int(input(">> Masukkan angka pertama: "))
angka2 = int(input(">> Masukkan angka kedua: "))

# apabila angka 1 atau 2 bernilai 5, dan angka1 ditambah angka2 hasilnya 5, dan angka1 dikurang angka2 hasilnya 5
if (angka1 == 5 or angka2 == 5) and (angka1 + angka2 == 5) and (angka1 - angka2 == 5) :
    print("Salah satu atau kedua angka yang kamu masukin itu ada 5 nya, terus kalau dijumlah hasilnya 5, dikurang juga hasilnya 5. Bener kan? ")
elif angka1 == 5 or angka2 == 5 :
    print("Salah satu atau kedua angka yang kamu masukin, pasti ada angka 5, yakan?")
elif angka1 + angka2 == 5 : 
    print("Hasil penjumlahan 2 angka yang kamu masukin hasilnya 5!")
elif angka1 - angka2 == 5 :
    print("Hasil pengurangan 2 angka yang kamu masukin hasilnya 5!")
else : 
    print("Salah satu atau keduanya, hasil penjumlahan dan pengurangannya, gaada nih yang cocok sama angka 5 :(")
    