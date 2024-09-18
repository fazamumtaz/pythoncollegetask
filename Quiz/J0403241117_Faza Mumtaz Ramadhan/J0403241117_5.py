W = float(input())
S = input()
kategori_berat = ""

if W > 0 :
    if W <= 1 :
        kategori_berat = "ringan"
    elif W <= 5 :
        kategori_berat = "sedang"
    else :
        kategori_berat = "berat"


if kategori_berat == "ringan" :
    if S == "E" :
        print(10000)
    elif S == "S" :
        print(15000)
    else :
        print(25000)
elif kategori_berat == "sedang" :
    if S == "E" :
        print(20000)
    elif S == "S" :
        print(25000)
    else :
        print(40000)
else :
    if S == "E" :
        print(30000)
    elif S == "S" :
        print(35000)
    else :
        print(50000)
