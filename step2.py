# pseudo koda dayalı çözüm
total_cupcakes = 28

for david in range(total_cupcakes + 1):
    for emma in range(total_cupcakes + 1):
        for frank in range(total_cupcakes + 1):
            
            # Şartları kontrol et
            cond1 = emma == (david + 3)
            cond2 = frank == (3 * david)
            cond3 = (david + emma + frank) == total_cupcakes
            
            if cond1 and cond2 and cond3:
                print(f"David packed {david} cupcakes!")
                print(f"Emma packed {emma} cupcakes!")
                print(f"Frank packed {frank} cupcakes!")
                break # Çözüm bulundu, aramayı durdur