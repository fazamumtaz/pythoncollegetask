# Pilih bangun datar yang ingin diketahui luasnya
option = int(input("Kamu mau menghitung luas apa: \n1. Segitiga \n2. Lingkaran \n3. Persegi / Bujur sangkar \n>> "))

# Kerjakan berdasarkan input user
if option == 1:
    # Menjalakan perhitungan Segitiga
    alas, tinggi = int(input(">> Masukkan nilai angka dalam centimeter: ")), int(input(">> Masukkan nilai tinggi dalam centimeter: "))
    hasil = 1/2 * alas * tinggi
    print(f"Luas segitiga yang ingin kamu tahu adalah {hasil}cm²")
elif option == 2:
    # Menjalakan perhitungan Lingkaran
    jariJari = int(input(">> Masukkan nilai jari-jari dalam centimeter: "))
    hasil = 3.14 * jariJari**2
    print(f"Luas lingkaran yang ingin kamu ketahui adalah {hasil}cm²")
elif option == 3:
    # Menjalakan perhitungan persegi
    sisi = int(input(">> Masukkan nilai sisi persegi dalam centimeter: "))
    hasil = sisi**2
    print(f"Luas persegi yang ingin kamu ketahui adalah {hasil}cm²")
else : 
    # Print error karena gaada di opsi
    print("Gaada opsi yang kamu pilih :(")