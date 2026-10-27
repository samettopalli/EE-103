# multiply-all.py

start = int(input("Start number: "))
end = int(input("End number: "))

# For Döngüsü
result_for = 1
for i in range(start, end + 1):
    result_for *= i
print(f"Result with for loop: {result_for}")

# While Döngüsü
result_while = 1
current = start
while current <= end:
    result_while *= current
    current += 1
print(f"Result with while loop: {result_while}")

# Sanity Check
if result_for == result_while:
    print("results are same")
else:
    print("results are different")