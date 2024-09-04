# Masukkan huruf yang ingin diketahui vocal atau bukan
huruf = input("Masukkan sebuah huruf: ")

# Cek apakah huruf yang diinput 1 atau bukan, dan cek apakah itu huruf
vocal = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
if huruf in vocal :
    print(f"Benar, {huruf} adalah huruf vokal")
else : 
    print(f"Salah, {huruf} bukanlah huruf vokal")