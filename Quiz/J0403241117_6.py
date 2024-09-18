paket = input()
hari = input()

weekday = ["senin", "selasa", "rabu", "kamis", "jumat"]
weekend = ["sabtu", "minggu"]

kategori_hari = "weekday"

if hari in weekend :
   kategori_hari = "weekend"
else :
   ""

if paket == "A" :
   if kategori_hari == "weekday" :
      print(50000)
   else :
      print(60000)
elif paket == "B" :
   if kategori_hari == "weekday" :
      print(70000)
   else :
      print(80000)
else :
   if kategori_hari == "weekday" :
      print(90000)
   else :
      print(100000)


