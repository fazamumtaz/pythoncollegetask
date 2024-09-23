# 1. range(x)
# 2. range(x, y)
# 3. range(x, y, z)
menu = ['uduk', 'kuning', 'bubur'] #len 3
# for i in range(len(menu)) :
#    print(menu[i])
# for makanan in menu :
#    print(makanan)
# for i in 'indonesia' :
#    print(i)

# i = 0
# while i < len(menu) :
#    print(menu[i])
#    i += 1

# Segitiga
# for i in range(1, 11): #2
#    for j in range(1, i + 1) : #2
#       print("%d " % (i * j), end=' ') 
#    print()



surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()[::-2].upper()  
print(surprise[-1])

print('\n')
