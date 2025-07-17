import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Version
# randomly choose letters, symbols, and numbers from the lists. Then combine the entire list into a single string. Use String concatenation to create the generated password.
# random_letters = "".join(random.sample(letters, nr_letters))
# random_symbols = "".join(random.sample(symbols, nr_symbols))
# random_numbers = "".join(random.sample(numbers, nr_numbers))
# generated_password = random_letters + random_symbols + random_numbers
# 
# print(f"Your generated password is: {generated_password}")

# Hard Version
# In the hard version, we will create 3 empty strings for letters, symbols, and numbers. 
# Then we will use for loops to iterate through the number of letters, symbols, and numbers chosen by the user by using the range function.
# and each time we will add a random character to each string by picking a random character 
# from each list by using the random.choice() function and using the addition assignment operator to add the character to the string.
# Finally, we will use string concatenation to combine the letters, symbols, and numbers to create the generated password.
# To make the password more secure, we will shuffle them by creating an empty string and using the .join() method to convert the 
# list of characters made by the random.sample() function (which took the string and placed each character into a list at a random index because
# we used the len function to get the length of the generated password so that it shuffled all characters) into a string.
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