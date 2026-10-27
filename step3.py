# binary-integers.py

num = int(input("Enter an integer: "))
binary_rep = ""
temp = num

if temp == 0:
    binary_rep = "0"
    
while temp > 0:
    remainder = temp % 2
    binary_rep = str(remainder) + binary_rep # Kalanı başa ekle
    temp = temp // 2 # Tam sayı bölmesi yap

print(f"Binary representation of {num} is {binary_rep}")