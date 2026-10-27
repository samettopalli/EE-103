kelime = "elektronik"
bulundu = False 

for harf in kelime:
    if harf in"eE":
        bulundu = True 
        break

if bulundu:
    print("Aranan harf kelimede var !")
else:
    print("Aranan harf kelimede yok!")
        

