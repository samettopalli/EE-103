# 1000 bilet için sadece Alyssa'yı tahmin ederek döngü sayısını azaltıyoruz
for alyssa in range(1001):
    # Ben ve Cindy'nin bilet sayılarını Alyssa'ya göre doğrudan hesapla
    ben = alyssa - 2
    cindy = alyssa * 2
    
    # Toplam bilet sayısını kontrol et
    if alyssa + ben + cindy == 1000:
        print(f"Toplam 1000 bilet satıldığında Alyssa {alyssa} bilet satmıştır.")
        break  # Sonucu bulduğumuzda döngüyü erkenden bitir (optimizasyon)