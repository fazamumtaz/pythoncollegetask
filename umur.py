# Variabel input
nama = "Budi"
umur_sekarang = int(input('umur skrg'))
tahun_sekarang = int(input('tahun sekarang'))
umur_target = int(input('umur brp di tahun brp'))

harga = 50000

# Menghitung tahun saat Budi berumur 50 tahun
tahun_saat_umur_target = tahun_sekarang + (umur_target - umur_sekarang)

# Output hasil
print(f"{nama} akan berumur {umur_target} tahun pada tahun {tahun_saat_umur_target}.")
print(nama, "akan berumur", umur_target, "tahun pada tahun", tahun_saat_umur_target)
print("Rp", harga) #Rp 50000
print(f"Rp{harga}") #Rp50000
