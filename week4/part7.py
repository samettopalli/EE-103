number = 13
binary_result = ""

# Sayı 0'dan büyük olduğu sürece 2'ye böl
while number > 0:
    remainder = number % 2
    # Bulduğumuz kalanı string'in en başına ekliyoruz (ters çevirme adımı)
    binary_result = str(remainder) + binary_result 
    number = number // 2  # Tam sayı bölmesi ile sayıyı güncelle

print(f"13 sayısının binary hali: {binary_result}")