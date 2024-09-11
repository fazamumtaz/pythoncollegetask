nilUAS = int(input("UAS = "))
nilUASP = int(input("UASP = "))
nilUTS = int(input("UTS = "))
nilUTSP = int(input("UTSP= "))

# Menghitung nilai akhir 
nilaiAkhir = (nilUAS * 0.4) + (nilUASP * 0.15) + (nilUTS * 0.3) + (nilUTSP * 0.15)

if nilaiAkhir <= 100:
    if nilaiAkhir >= 80:
        hurufMutu = 'A'
    elif nilaiAkhir >= 70:
        hurufMutu = 'B'
    elif nilaiAkhir >= 60:
        hurufMutu = 'C'
    elif nilaiAkhir >= 40:
        hurufMutu = 'D'
    else : 
        hurufMutu = 'E'
else: 
    hurufMutu = "Nilai nguawor"

# if 80 <= nilaiAkhir <= 100:
#     hurufMutu = 'A'
# elif 70 <= nilaiAkhir < 80:
#     hurufMutu = 'B'
# elif 60 <= nilaiAkhir < 70:
#     hurufMutu = 'C'
# elif 40 <= nilaiAkhir < 60:
#     hurufMutu = 'D'
# elif 0 <= nilaiAkhir < 40:
#     hurufMutu = 'E'
# else : 
#     hurufMutu = 'Tidak Valid'

print(f"Nilai akhir: {nilaiAkhir}\nHuruf Mutu: {hurufMutu}")