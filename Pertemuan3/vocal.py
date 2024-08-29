# Masukkan huruf yang ingin diketahui vocal atau bukan
huruf = input(">> Masukkan satu huruf: ")

# Cek apakah huruf yang diinput 1 atau bukan, dan cek apakah itu huruf
if len(huruf) == 1 and huruf.isalpha() : 
    vocal = ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']
    if huruf in vocal :
        print(f"Huruf yang kamu masukkan: {huruf}, adalah huruf vokal!")
    else : 
        print("Huruf yang kamu masukkan, bukanlah huruf vokal")
else : print("Kamu hanya bisa memasukkan 1 huruf dan tidak bisa memasukkan simbol :>")