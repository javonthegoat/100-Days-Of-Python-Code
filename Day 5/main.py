import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version
# random_letters = "".join(random.sample(letters, nr_letters))
# random_symbols = "".join(random.sample(symbols, nr_symbols))
# random_numbers = "".join(random.sample(numbers, nr_numbers))
# generated_password = random_letters + random_symbols + random_numbers
# 
# print(f"Your generated password is: {generated_password}")

# Hard Version
random_letters = ""
random_symbols = ""
random_numbers = ""

for number in range(0, nr_letters):
    random_letters += random.choice(letters)

for number in range(0, nr_symbols):
    random_symbols += random.choice(symbols)

for number in range(0, nr_numbers):
    random_numbers += random.choice(numbers)

generated_password = random_letters + random_symbols + random_numbers
shuffled_password = "".join(random.sample(generated_password, len(generated_password)))

print(f"Your generated password is: {shuffled_password}")