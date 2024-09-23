# WHILE ---
# Lakukan selama kondisi bernilai true dan berhenti jika kondisi bernilai false
# i = 5 
# while i < 10 :
#    print("$", end = " ")
#    i += 1
# print('\n')

# FOR --- 
# Biasanya digunakan untuk ngambil data/item yang ada di list, tuple, string, dictionary ataupun set
# Digunakan menggunakan fungsi range()
# 1. Apabila string, maka dia akan mengambil karakter dari setiap huruf

# for i in 'Dasar Pemrograman' :
#    print(i, end = " ")

# # 2. Apabila berupa list/koleksi maka dia akan mengambil nilai dari indexnya

mata_pelajaran = ['Matematika', 'Fisika', 'Biologi']

# for i in mata_pelajaran :
#    print(i, end = " ")

# print('\n')

# for i in range(len(mata_pelajaran)) :
#    print(mata_pelajaran[i])

# i = 0
# while i < len(mata_pelajaran) :
#    print(mata_pelajaran[i])
#    i += 1

# Segitiga
# for i in range(1,11):
#    for j in range(1, i+1):
#       print("%d " % (i*j), end=' ')
#    print()

data_makanan = ['Cheetos', 'Samyang', 'Lays', 'PotaBee']
# for snack in data_makanan : 
#    if snack == 'Lays' :
#       continue
#    print(snack)

# for i in range(len(mata_pelajaran)) :
#    print(mata_pelajaran[i])
# else : 
#    print('Semua mata pelajaran sudah ditampilkan')

# i = 0 
# while i < len(data_makanan) :
#    print(data_makanan[i])
#    i += 1
# else :
#    print('Semua menu yang ada sudah ditampilkan')

# n = 10  # number of Fibonacci numbers to generate
# a, b = 0, 1  # initial two numbers in the Fibonacci sequence

# for _ in range(n):
#    print(a, end=' ') # 0 1 1 2 3 
#    a, b = b, a + b

# angka = int(input()) 

# if angka > 0 :
#    for others in range(2, angka) :
#       if angka % others == 0 :
#             print(f"{angka} bukan merupakan angka prima")
#             break
#    else : 
#       print(f"{angka} merupakan bilangan prima")
# else :
#    print(f"{angka} bukan merupakan bilangan prima")

# MENGHITUNG HURUF VOKAL
# kata = input() #belajar
# vokal = 'aiueoAIUEO'
# berapa = 0
# for huruf in kata :
#    if huruf in vokal :
#       berapa += 1



# bilangan=int(input("Masukkan nilai bilangan:"))
# pangkat= int(input("Masukkan nilai pangkat:")) 
# hasil = 1
# for i in range(0): 
#    hasil = hasil * bilangan
#    print("hasil perpangkatan ke-",i, "=", hasil)


# print("hasil perpangkatan:", hasil)






# print(berapa)

# PANGKAT MANUAL
# angka = int(input("Masukkan angka: ")) #2
# pangkat = int(input("Masukkan pangkat: ")) #3

# i = 1
# hasil = 1

# if pangkat == 0 :
#    hasil = 1
# else :
#    while i <= pangkat :
#       hasil = hasil * angka
#       i += 1

# print(hasil)

hurufPengganti = input() # i
kata = input() # vokal
vokal = 'aiueoAIUEO'
katabaru = ""
for huruf in kata :
   if huruf in vokal :
      katabaru += hurufPengganti
   else :
      katabaru += huruf

print(katabaru)

# TUPLE
# datadiri = ('Faza Mumtaz', 'Faza', 'J0403241117')
# nama, nick, nim = datadiri

# print(f"Nama: {nama}\nNama panggilan: {nick}\nNIM: {nim}")
