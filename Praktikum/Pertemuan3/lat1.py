bil = int(input())

# Pengecekah bilangan kurang, lebih, sama dengan 10 
# if bil > 10 :
#     print(bil, "lebih besar daripada 10")
# elif bil == 10 :
#     print(bil, "sama dengan 10")
# else :
#     print(bil, "kurang daripada 10")

# Pengecekan bilangan ganjil/genap, positif/negatif

if bil % 2 == 0 :
    if bil >= 0 :
        print(bil, "adalah bilangan genap positif")
    else :
        print(bil, "adalah bilangan genap negatif")     
else :
    if bil >= 0 :
        print(bil, "adalah bilangan ganjil positif")
    else :
        print(bil, "adalah bilangan ganjil negatif")