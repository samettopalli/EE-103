x = float(input("Karekökü alınacak sayıyı girin: "))
guess = x / 2.0  # Başlangıç tahmini

# Tahminin karesi ile x arasındaki fark 0.001'den büyük olduğu sürece döngü çalışır
while abs(guess**2 - x) >= 0.001:
    guess = (guess + x / guess) / 2.0

print(f"{x} sayısının karekökü yaklaşık olarak: {guess}")