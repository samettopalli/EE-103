hedef = 24
epsilon = 0.01

tahmin = hedef / 2.0
adım_sayisi = 0

while abs(tahmin**2 - hedef) >= epsilon:
    adım_sayisi += 1
    tahmin = tahmin - (tahmin**2 - hedef) / (2 * tahmin)

print(f"{hedef} sayısının karekökü yaklaşık: {tahmin}")
print(f"Toplam adım sayısı: {adım_sayisi}")