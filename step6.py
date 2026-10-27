input_prompt = float(input("Enter a number to find the square root: "))

epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

# Hem hata payını (epsilon) hem de overshoot (aşma) durumunu kontrol et
while abs(guess**2 - input_prompt) >= epsilon and guess**2 <= input_prompt:
    guess += increment
    num_guesses += 1
    
    # Hata ayıklama (Debug) için her 1000. tahmini yazdır
    if num_guesses % 1000 == 0:
        print(f"Current guess = {guess}")

print(f"\nTotal guesses: {num_guesses}")
print(f"Approximated square root: {guess}")