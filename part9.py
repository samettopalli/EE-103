hedef = 0.5
epsilon = 0.01

if hedef >= 1:
    low = 0.0
    high = hedef
else:
    low = hedef
    high = 1.0

tahmin = (low + high) / 2

while abs(tahmin**2 - hedef) >= epsilon:
    if tahmin**2 < hedef:
        low = tahmin
    else:
        high = tahmin
        
    tahmin = (low + high) / 2

print(f"{hedef} sayısının karekökü yaklaşık: {tahmin}")