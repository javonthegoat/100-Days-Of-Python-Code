import random

heads_tails = int(input("Pick one heads or tails. Type '1' for heads or '2' for tails: "))
computer_flip = random.randint(1, 2)

if heads_tails == computer_flip:
    user_won = True
else:
    user_won = False

if computer_flip == 1:
    print("The coin landed on heads.")
elif computer_flip == 2:
    print("The coin landed on tails.")

if user_won:
    print("You won!")
else:
    print("You lost!")