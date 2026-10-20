# Toplam 10 bilet olduğu için her biri en fazla 10 satmış olabilir
for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            # Soruda verilen denklemleri kontrol et
            if ben == alyssa - 2 and cindy == alyssa * 2:
                # Toplam satılan bilet sayısı 10 mu?
                if alyssa + ben + cindy == 10:
                    print(f"Toplam 10 bilet satıldığında Alyssa {alyssa} bilet satmıştır.")