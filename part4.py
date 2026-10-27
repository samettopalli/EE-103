isim = "Samet"
bölüm = "Elektronik"
print(f"Benim adım {isim} ve benim bölümüm {bölüm}")

doğum_yili = int(input("Doğum yılınızı girin:"))

yaş = 2026 - doğum_yili
if yaş<18:
    print("ehliyet alamaz")
elif yaş == 18 :
    print("ehliyet alabilirsin")
else :
    print("sen zaten ehliyet alabilecek yaştasın")
