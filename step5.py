# binary-fractions.py

fraction = float(input("Enter a fraction (e.g. 0.375): "))
binary_rep = "0."

# Sonsuz döngüyü engellemek için sınır belirliyoruz
while fraction > 0 and len(binary_rep) < 20:
    fraction *= 2
    int_part = int(fraction) # Sadece tam kısmı al (0 veya 1)
    binary_rep += str(int_part)
    fraction -= int_part # Tam kısmı çıkararak ondalıklı kısımla devam et
    
    # 0.1 gibi devirli sayılar için durdurma toleransı
    if abs(fraction) < 0.00001: 
        break

print(f"Binary representation: {binary_rep}")