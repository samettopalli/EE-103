x = 0
for i in range(10):
    print(x)
    x = x + 0.1

print("Sonuç neden 1.0 değil de 0.999999... çıkıyor?")
print("Açıklama: Bilgisayarlar ondalıklı sayıları (float) ikili (binary) sistemde saklar.")
print("0.1 gibi bazı ondalık sayılar ikili sistemde tam karşılık bulamaz ve sonsuz devreden bir kesire dönüşür.")
print("Bu nedenle hafızada saklanırken çok küçük bir yuvarlama hatası oluşur ve bu hatalar toplandıkça gözle görülür hale gelir.")