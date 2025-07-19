import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)

placeholder = ""

for letter in chosen_word:
    placeholder += "_"
print("Word to guess: " + placeholder)

letters_guessed = []
display = ""
guessing = True

while guessing:
    print(f"Lives Remaining: {lives}")
    guess = input("Guess a letter: ").lower()

    if guess in letters_guessed:
        print(f"You've already guessed letter: {guess}")

    letters_guessed.append(guess)

    for index in range(0, len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display = display[:index] + letter + display[index+1:]
        elif letter in display:
            continue
        else:
            display = display[:index] + "_" + display[index+1:]

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess} that is not in the word. -1 Life.")
        if lives == 0:
            guessing = False
            print("You ran out of lives.")

            print(f"You Lose. The word was {chosen_word}")

    if "_" not in display:
        guessing = False
        print(f"You guessed the word {display}!")
        print("YOU WIN!")

    print(stages[-lives-1])