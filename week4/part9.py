fraction = 0.1
target = 0.1
binary_str = "0."

# Çıkan binary sonucun ondalık sistemde neye karşılık geldiğini tutacak değişken
current_decimal_value = 0.0 
multiplier = 0.5  # Her bir bitin değeri sırasıyla 1/2, 1/4, 1/8...

# Hedef değere (0.1) olan uzaklığımız 0.00001'den büyük veya eşit olduğu sürece devam et
while abs(current_decimal_value - target) >= 0.00001:
    fraction *= 2
    bit = int(fraction)
    binary_str += str(bit)
    fraction -= bit
    
    # Elde edilen bit değerini toplam ondalık değerimize ekle
    current_decimal_value += bit * multiplier
    multiplier /= 2  # Bir sonraki bitin ağırlığı yarısı olacak

print(f"0.1'in hesaplanan binary değeri (hata payı ile): {binary_str}")