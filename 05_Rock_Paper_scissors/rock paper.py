import numpy as np
import random as rd

ask_keyword = input("Input the keyword for your password: ")
while True:
    try:
        ask_len = int(input("Input the length of your password: "))
        ask_character = int(input("Input the number of characters for your password: "))
        ask_num = int(input("Input the number of numbers for your password: "))
        ask_symbol = int(input("Input the number of symbols for your password: "))
        
        if ask_len < ask_character + ask_num + ask_symbol:
            print("The sum of characters, numbers and symbols cannot exceed the total password length.")
            continue
        
        break
    except ValueError:
        print("Please input a number")
    except Exception as e:
        print(f"An error occurred: {e}")

spl_charc = ["@", "#", "!", "$", "%", "^", "*", "-", "+"]
spl_symbol = rd.sample(spl_charc, ask_symbol)

password = list(ask_keyword)

# Add characters
for _ in range(ask_character):
  password.append(chr(rd.randint(97,122))) # Lowercase letters
  
# Add numbers
for _ in range(ask_num):
  password.append(str(rd.randint(0,9)))

# Add symbols
for symbol in spl_symbol:
  password.append(symbol)

# Add remaining random characters to reach desired length
remaining_length = ask_len - len(password)

for _ in range(remaining_length):
    password.append(rd.choice(password)) # Randomly select from existing characters for more unpredictability

rd.shuffle(password)
print("".join(password))