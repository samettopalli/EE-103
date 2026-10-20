fraction = 0.375
binary_fraction = "0."

# Kesir sıfırlanana kadar işlemi tekrarla
while fraction > 0:
    fraction *= 2
    # Tam sayı kısmını al (0 veya 1)
    integer_part = int(fraction)
    binary_fraction += str(integer_part)
    # Tam sayı kısmını çıkararak sadece yeni kesirli kısmı bırak
    fraction -= integer_part

print(f"0.375 sayısının binary hali: {binary_fraction}")