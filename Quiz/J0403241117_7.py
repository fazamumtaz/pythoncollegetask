# Inisiasi dan input
bilbul = int(input()) #bilbul = bilangan bulat
romawi = ""

# hal yang terjadi : 
# 1. Cek apakah bilbul termasuk ke dalam salah satu kondisi
# 2. Ketika masuk suatu kondisi, bilbul akan di cek berapa pengulangan romawi terbesar yang dapat dilakukan melakukan operasi //
# 3. Angka romawi akan dicetak sebanyak pengulangan yang bisa dilakukan 
# 4. bilbul akan dikurangi sebanyak angka romawi yang sementara tercetak
# 5. Cek apakah sisa dari kondisi pertama dapat masuk kembali ke dalam suatu kondisi, apabila  iya, akan terjadi siklus sampai tidak cocok dengan kondisi apapun

if bilbul >= 1000 :
    pengulangan = bilbul // 1000 
    romawi = romawi + "M" * pengulangan
    bilbul = bilbul - 1000 * pengulangan

if bilbul >= 500 :
    pengulangan = bilbul // 500 
    romawi = romawi + "D" * pengulangan
    bilbul = bilbul - 500 * pengulangan

if bilbul >= 100 :
    pengulangan = bilbul // 100 
    romawi = romawi + "C" * pengulangan
    bilbul = bilbul - 100 * pengulangan

if bilbul >= 50 :
    pengulangan = bilbul // 50 
    romawi = romawi + "L" * pengulangan
    bilbul = bilbul - 50 * pengulangan

if bilbul >= 10 :
    pengulangan = bilbul // 10
    romawi = romawi + "X" * pengulangan
    bilbul = bilbul - 10 * pengulangan

if bilbul >= 5 :
    pengulangan = bilbul // 5
    romawi = romawi + "V" * pengulangan
    bilbul = bilbul - 5 * pengulangan

if bilbul >= 4 :
    pengulangan = bilbul // 4
    romawi = romawi + "IV" * pengulangan
    bilbul = bilbul - 4 * pengulangan

if bilbul >= 1 :
    pengulangan = bilbul // 1
    romawi = romawi + "I" * pengulangan
    bilbul = bilbul - 1 * pengulangan

print(romawi)