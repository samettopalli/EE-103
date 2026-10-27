gizli_sifre = "1234"
tahmin = input("Şifrenizi girin: ")
while tahmin != gizli_sifre:
    tahmin = input("Hatalı şifre! Tekrar deneyin:")

print("Tebrikler, doğru şifre!")

