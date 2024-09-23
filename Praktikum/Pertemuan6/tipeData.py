# 1. Buatlah suatu list bernama years_list, dimulai dengan tahun kelahiran anda, dan
# seterusnya sampai tahun saat anda berumur 5 tahun. Sebagai contoh, jika anda lahir
# pada 1980. List years_list = [1980, 1981, 1982, 1983, 1984, 1985].
# • Pada taun berapakah dalam years_list anda berumur 3 tahun?
# • Pada tahun berapakah dalam years_list anda paling tua?

years_list = [2005, 2006, 2007, 2008, 2009, 2010, 2011]
print(years_list[-3]) # saya berumur 3 tahun
print(years_list[-1]) # saya paling tua dari tahun yang tertera pada list
print(years_list[1:5:2]) # saya paling tua dari tahun yang tertera pada list

print('\n')

# 2. Buatlah suatu list bernama things dengan 3 string ini sebagai elemennya: "mozzarella",
# "cinderella", "salmonella".
# • Huruf besarkan elemen dalam things yang merujuk ke seseorang dan kemudian
# cetak list tersebut. Apakah itu mengubah elemen di dalam list?
# • Buatlah elemen “cheesy” dari things menjadi huruf besar dan kemudian cetak list.
# • Hapus elemen “disease” dari things dan cetak list.

things = ['mozzarella', 'cinderella']
things[1] = things[1].upper() # mengubah menjadi kapital
things[0] = things[0].upper() # mengubah menjadi kapital
penyakit = things.pop(-1) # menghapus penyakit

print('\n')

# 3. Buatlah suatu list bernama surprise dengan elemen: "Groucho", "Chico", and "Harpo".
# • Huruf-kecilkan elemen terakhir dari list surprise, balik hurufnya, dan kemudian
# besarkan.

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()[::-1].upper()  
print(surprise[-1])

print('\n')

# list tuple set dictionary
# datadiri = ('Faza', 18, 'TPL')
# nama, umur, jurusan = datadiri
# print(f"nama saya adalah {nama}, saya berumur {umur}tahun, dan saya merupakan mahasiswa jurusan {jurusan}")

# 4. Buatlah suatu kamus English-to-Indonesia bernama e2i dan cetaklah. Kata-kata awal
# yang harus ada: dog = anjing, cat = kucing, dan tiger = macan.
# • Menggunakan kamus tiga kata e2i, cetak kata Indonesia dari tiger.
# • Buatlah kamus Indonesia-to-English bernama i2e dari e2i.
# • Gunakan i2e, cetak kata English yang Indonesianya dalah kucing.
# • Buat dan cetak sehimpunan kata English dari kunci dalam e2i.
e2i = {
   'tiger' : 'macan',
   'cat' : 'kucing',
   'dog' : 'anjing'
}

#mengakses value dalam dictionary, menggunakan nama_dictionary[key]

i2e = {}
for key in e2i : # membalik key-value dari e2i menjadi value-key
   value = e2i[key]
   i2e[value] = key

print(e2i['tiger'])
print(i2e['kucing'])
for key in e2i :
   print(key)

print('\n')

# 5. Buatlah suatu kamus multilevel bernama life. Gunakan string ini untuk kunci level
# tertinggi: 'animals', 'plants’, dan 'other’. Buatlah kunci 'animals’ merujuk ke kamus lain
# dengan kunci 'cats', 'octopi’, dan 'emus’. Buatlah kunci 'cats’ merujuk ke suatu list
# string dengan nilai 'Henri', 'Grumpy’, dan 'Lucy’. Buatlah semua kunci lain merujuk ke
# kamus kosong.
# • Cetak kunci top-level dari life.
# • Cetak kunci untuk life['animals’].
# • Cetak nilai untuk life['animals']['cats'].

life = {
   'animals' : {
      'cats' : ['Henri', 'Grumpy', 'Lucy'],
      'octopi' : {},
      'emus' : {}
   },
   'plants' : {},
   'other' : {}
}
for key in life : # cetak key dari life
   print(key)

for key in life['animals'] : # cetak key dari life : animals
   print(key)

for key in life['animals']['cats'] : # cetak key dari life : animals : cats
   print(key)
   
print('\n')