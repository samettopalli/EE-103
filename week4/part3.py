s = "abcabc"
unique_letters = ""

for char in s:
    # Eğer harf daha önce unique_letters içine eklenmediyse, ekle
    if char not in unique_letters:
        unique_letters += char

# Benzersiz harflerin sayısını yazdır
print("Benzersiz karakter sayısı:", len(unique_letters))
