sayi1 = 0.1 + 0.1 +0.1 
sayi2 = 0.3
epsilon = 0.001
if abs(sayi1 -sayi2)  < epsilon:
    print("Sayılar birbirine yeterince yakın")

sayi1 = 0.1 + 0.1 + 0.1
sayi2 = 0.3
fark = abs(sayi1 - sayi2)

print(f"sayi1 değeri : {sayi1}")
print(f"sayi2 değeri : {sayi2}")
print(f"Aralarındaki Fark: {fark}")

hedef = 2
epsilon = 0.01
adim = 0.001
tahmin = 0.0

while abs(tahmin**2  - hedef) >= epsilon:
    tahmin = tahmin + adim

print(f"2'nin karekökü yaklaşık: {tahmin}")

hedef = 2
epsilon = 0.0001  
adim = 0.01      
tahmin = 0.0

while abs(tahmin**2 - hedef) >= epsilon and tahmin**2 <= hedef:
    tahmin = tahmin + adim

if abs(tahmin**2 - hedef) < epsilon:
    print(f"Başarılı! Karekök yaklaşık: {tahmin}")
else:
    print("Hedef aşıldı! Bu adım boyuyla uygun karekök bulunamadı.")