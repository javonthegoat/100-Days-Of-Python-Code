import random
import os
import time

player_attempts = 0
number_to_guess = random.randint(1,100)

def clear_console():
    if os.name == 'nt':  # this is a windows operating system
        os.system('cls')
    else:  # this is for macOS, linux, debian, etc
        os.system('clear')

def reset_number_to_guess():
    global number_to_guess
    number_to_guess = random.randint(1,100) # set number_to_guess to a random whole number between 1 and 100

# reduce attempts by 1
def deduct_attempt():
    global player_attempts
    player_attempts -= 1
    print(f"You have {player_attempts} attempts left.")

def adjust_attempts():
    global player_attempts
    if difficulty == "easy": # set attempts to 10 
        player_attempts = 10
        print("You have 10 attempts.")
    elif difficulty == "hard": # set attempts to 5
        player_attempts = 5
        print("You have 5 attempts.")

def number_matched(number):
    if number == number_to_guess: # the guess matches the number to guess
        return True
    elif number > number_to_guess: # the guess is over the number to guess
        print("Too high!")
    elif number < number_to_guess: # the guess is under the number to guess
        print("Too low!")
    return False

playing_game = True

while playing_game:
    print(f"Debug: the number is {number_to_guess}")
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. easy: 10 attempts, hard: 5 attempts: ").lower()
    adjust_attempts() # set the number of attempts based on difficulty
    guess = int(input("Guess a number between 1 and 100: "))
    guessing = True
    while guessing:
        if number_matched(guess):
            print(f"You guessed the number! The number was {number_to_guess}")
            play_again = input("Would you like to play again? (y/n) ").lower()
            if play_again == "y":
                clear_console()
                reset_number_to_guess() # pick a new number between 1 and 100
                break
            else:
                # end the game
                guessing = False
                playing_game = False
        else:
            deduct_attempt()  # remove an attempt for every wrong guess
            if player_attempts > 0: # only make a guess again if the player has not ran out of attempts
                guess = int(input("Guess again: ")) 
            else:
                print(f"You ran out of guesses! The number was {number_to_guess}.") # reveal the number
                time.sleep(3) # wait 3 seconds before restarting the game
                clear_console()
                reset_number_to_guess() # pick a new number between 1 and 100
                break