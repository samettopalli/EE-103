# Verilen metin (İsmin SAMET olduğu için metni ona göre tanımladık)
s = "Aho54yuSAMET42z.89tur"

# İsmin başlangıç ve bitiş indeksleri:
# "SAMET" kelimesi 7. indeksten başlar ve 12. indekse kadar gider.
name = s[7:12]

# İsmi f-string ile yazdırma
print(f"My name is {name}")

# İsmi ters çevirip f-string ile yazdırma ( [::-1] ifadesi metni ters çevirir )
reversed_name = name[::-1]
print(f"My name in reverse order is {reversed_name}")
