#  Input angka yang ingin diketahui hasil baginya dan modulusnya
angka = int(input(">> Masukkan angka yang kamu mau tau hasil bagi nya: "))
modulus = int(input(">> Masukkan angka sebagai modulus pembagi angka tersebut: "))

# Cek apakah modulus > 0 
if modulus > 0 :
    # Print hasil sisa bagi
    print("Sisa hasil bagi dari angka dan modulus tersebut adalah:", angka % modulus)
else :
    # Print error
    print("Modulus yang kamu masukin harus lebih besar dari 0")