metin = input("hata gözlerle anlatılmaz:")
metin_kucuk = metin.lower()
sesli_harfler = "aeö"
sayac = 0
for karakter in metin_kucuk:
    if karakter in sesli_harfler:
        sayac+= 1
print(f"Girdiğiniz metinde {sayac} adet sesli harf var.")