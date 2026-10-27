x = 25
epsilon = 0.01
alt_sinir = 0
ust_sinir = x
tahmin = (alt_sinir + ust_sinir) / 2

while abs(tahmin**2 - x) >= epsilon:
    if tahmin**2 < x:
        alt_sinir = tahmin
    else:
        ust_sinir = tahmin
    
    tahmin = (alt_sinir + ust_sinir) / 2

print(f"{x} sayısının yaklaşık karekökü: {tahmin}")