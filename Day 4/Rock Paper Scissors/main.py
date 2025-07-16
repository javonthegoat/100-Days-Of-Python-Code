import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# paper beats rock, scissors beats paper, and rock beats scissors.
choices = [rock, paper, scissors] # add the strings to a list in the order they will be asked
try:
    users_choice = choices[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))] # convert the input (which is a string) to an integer and index the choices list to get the string
except (ValueError, IndexError): # catch the value error for converting an invalid string to an integer and the index error for a number that is not in the range of the items in the choices list
    print("Invalid choice. Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    exit() # exit the program if the user enters an invalid choice
computer_choice = choices[random.randint(0,2)] # choose a random string from the choices list
print(f"{users_choice}\nComputer Chose:\n{computer_choice}") # print the user's choice and the computer's choice to the console
user_wins = False # check if the user wins
draw = False # check if it's a draw

if users_choice == computer_choice: # if the users and the computer make the same choice it's a draw.
    draw = True
elif users_choice == paper and computer_choice == rock: # paper beats rock
    user_wins = True
elif users_choice == scissors and computer_choice == paper: # scissors beats paper
    user_wins = True
elif users_choice == rock and computer_choice == scissors: # rock beats scissors
    user_wins = True

if user_wins:
    print("You Win!") # If the user wins print they won to the console
elif draw:
    print("It's a Draw.") # if the computer and the user made the same choice print it's a draw to the console
else:
    print("You Lose.") # If the user loses to the computer print you lost to the console
