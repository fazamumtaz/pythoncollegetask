tanggal = int(input("Masukkan tanggal lahir: "))
bulan = int(input("Masukkan bulan lahir (dalam angka): "))

if bulan == 3:
    if tanggal >= 21:
        zodiak = "Aries"
    else:
        zodiak = "Pisces"
elif bulan == 4:
    if tanggal <= 19:
        zodiak = "Aries"
    else:
        zodiak = "Taurus"
elif bulan == 5:
    if tanggal <= 20:
        zodiak = "Taurus"
    else:
        zodiak = "Gemini"
elif bulan == 6:
    if tanggal <= 20:
        zodiak = "Gemini"
    else:
        zodiak = "Cancer"
elif bulan == 7:
    if tanggal <= 22:
        zodiak = "Cancer"
    else:
        zodiak = "Leo"
elif bulan == 8:
    if tanggal <= 22:
        zodiak = "Leo"
    else:
        zodiak = "Virgo"
elif bulan == 9:
    if tanggal <= 22:
        zodiak = "Virgo"
    else:
        zodiak = "Libra"
elif bulan == 10:
    if tanggal <= 22:
        zodiak = "Libra"
    else:
        zodiak = "Scorpio"
elif bulan == 11:
    if tanggal <= 21:
        zodiak = "Scorpio"
    else:
        zodiak = "Sagittarius"
elif bulan == 12:
    if tanggal <= 21:
        zodiak = "Sagittarius"
    else:
        zodiak = "Capricorn"
elif bulan == 1:
    if tanggal <= 19:
        zodiak = "Capricorn"
    else:
        zodiak = "Aquarius"
elif bulan == 2:
    if tanggal <= 18:
        zodiak = "Aquarius"
    else:
        zodiak = "Pisces"
else:
    zodiak = "Tanggal atau bulan tidak valid"

print("Zodiak Anda adalah", zodiak)