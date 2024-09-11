#No 2
N = int(input())
if N % 2 == 1 and N > 0:
    print(N)
else :
    print(N, "bukan bilangan bulat ganjil positif")

#No 4

C = int(input())

if C < 0 :
    print("Dingin sekali")
elif C <= 20 :
    print("Dingin")
elif C <= 30 :
    print("Hangat")
else :
    print("Panas")

#No 5
# Ongkir berdasarkan berat dan jenis layanan. 
W = int(input())
S = input()
ongkos = 0
berat = ""

if W > 0:
    if W <= 1 :
        berat = "ringan"
    elif W <= 5 :
        berat = "sedang"
    else :
        berat = "berat"
else : 
    print("error")

if W == "ringan" :
    if S == "E" :
        ongkos = 10000
    elif S == "S" :
        ongkos = 15000
    else :
        ongkos == 25000
elif W == "sedang" :
    if S == "E" :
        ongkos = 20000
    elif S == "S" :
        ongkos = 25000
    else :
        ongkos == 40000
else :
    if S == "E" :
        ongkos = 30000
    elif S == "S" :
        ongkos = 35000
    else :
        ongkos == 50000

print(ongkos)


# No 7


