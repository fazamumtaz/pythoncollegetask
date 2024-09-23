a = int(input("masukkan bilangan ganjil lebih dari 50: "))

while a % 2 != 0 or a <= 50 :
   a = int(input("salah, coba ulangi lagi: "))

print("benar")