n = int(input("Enter a number: "))

# 1'den n'ye kadar olan sayıların döngü ile toplamı
running_sum = 0
for i in range(1, n + 1):
    running_sum += i

# Gauss formülü ile toplam: n * (n + 1) / 2
sum_gauss = n * (n + 1) // 2

# Sonuçları kontrol etme
if running_sum == sum_gauss:
    print("My running sum code works correctly")
else:
    print("My running sum code failed badly")