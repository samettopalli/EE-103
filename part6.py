hedef = int(input("Kaça kadar toplayalım?: "))
toplam = 0
for sayi in range(1, hedef + 1):
    if sayi % 2 == 0 :
        print(f"Çift sayı bulundu: {sayi}")

print(f"1 ile {hedef} arasındaki çift sayıların toplamı: {toplam}")