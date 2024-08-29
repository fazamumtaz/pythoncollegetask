# Input 3 angka yang ingin dibandingkan 
satu = int(input(">> Masukkan angka pertama: "))
dua = int(input(">> Masukkan angka kedua: "))
tiga = int(input(">> Masukkan angka ketiga: "))

# Urutkan angka-angka menggunakan sorted
# arr = [satu, dua, tiga]

# Ambil angka terkecil dan terbedar
# print("Angka terkecil yang kamu masukkan =", min(arr), "\ndan angka terbesar yang kamu masukkan =", max(arr))

# Mencari nilai terbesar
if satu >= dua and satu >= tiga :
    terbesar = satu
elif dua >= satu and dua >= tiga :
    terbesar = dua
else :
    terbesar = tiga

if satu <= dua and satu <= tiga :
    terkecil = satu
elif dua <= tiga and dua <= tiga :
    terkecil = dua
else : 
    terkecil = tiga 


print(f"Nilai terbesar yang kamu masukkan adalah {terbesar} \ndan nilai terkecil yang kamu masukkan adalah {terkecil}")
