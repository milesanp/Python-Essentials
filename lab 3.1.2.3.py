secret_number = 777

number = print(int(input(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")))

while number != 777 :
    if number == secret_number :
        print("Well done, muggle! You are free now.")
    else: 
        print("Ha Ha! you're stuck in my loop.")
    number = int(input(" What is my secret number?"))

print("Well done, muggle! You are free now.") 