# Kullanıcıdan x ve başlangıç tahmini g alınıyor
x = float(input("What x to find the cube root of? "))
g = float(input("What guess to start with? "))

# Mevcut tahminin küpü yazdırılıyor
print(f"Current estimate cube: {g**3}")

# Newton metodu ile bir sonraki tahmin hesaplanıyor
next_guess = g - (g**3 - x) / (3 * (g**2))

# Bir sonraki tahmin yazdırılıyor
print(f"Next guess: {next_guess}")
