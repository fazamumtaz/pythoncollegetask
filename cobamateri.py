list_a = [10, 2, 7, 4, 5]
j = 0 
while j < len(list_a) :
   if list_a[j] % 2 == 0 :
      list_a[j] = "genap"
   j += 1

print(list_a)