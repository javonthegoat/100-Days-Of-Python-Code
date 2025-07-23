import random

deck_of_cards = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]

def retrieve_cards():
    player_cards = random.sample(deck_of_cards, 2)
    computer_cards = random.sample(deck_of_cards, 2)
    return player_cards, computer_cards

def add_card_to_deck(deck):
    deck.append(random.choice(deck_of_cards))

def determine_a_winner(player_cards, computer_cards, player_score, computer_score):
    player_num_of_cards = len(player_cards)
    computer_num_of_cards = len(computer_cards)
    player_final_hand = f"Your final hand: {player_cards}, final score: {player_score}"
    computer_final_hand = f"Computer final hand: {computer_cards}, final score: {computer_score}"
    player_won = False

    if 11 in player_cards and player_score > 21: # Player has an ace (11) but there score is over 21 so the ace becomes a 1
        replace_ace = player_cards.index(11)
        player_cards[replace_ace] = 1
        print(f"Your score went over 21 but you had an ace.")
    if player_score > 21: # player's score is over 21
        print("Your score exceeded 21. You Lose!")
    elif player_num_of_cards == 2 and player_score == 21: # Player has a blackjack
        if computer_num_of_cards == 2 and computer_score == 21: # Player and Computer has a blackjack
            print(f"{player_final_hand}\n{computer_final_hand}")
            print("It's a tie, computer and user has a blackjack. You lose.")
        else:
            player_won = True
            print(f"{player_final_hand}\n{computer_final_hand}") # Player has a blackjack but computer doesn't
            print("You win! You have a blackjack.")
    elif player_score == computer_score: # It's a tie computer and player's score is the same
        print(f"{player_final_hand}\n{computer_final_hand}")
        print("It's a tie! You lose.")
    elif computer_num_of_cards == 2 and computer_score == 21: # Computer has a blackjack and user doesn't
         print(f"{player_final_hand}\n{computer_final_hand}")
         print("You lose. Computer has a blackjack")
    elif player_score > computer_score: # player's score is < 22 and over computer score and neither of them have a blackjack
        player_won = True
        print(f"{player_final_hand}\n{computer_final_hand}")
        print("You win! your score is higher than computer's score.")
    elif player_score < computer_score and computer_score > 21: # player's score is less than 22 but computer score exceeds 21
        player_won = True
        print(f"{player_final_hand}\n{computer_final_hand}")
        print("You win! computer's score exceeded 21")
    else:
        print(f"{player_final_hand}\n{computer_final_hand}") # computer has a higher score than the player and neither has a blackjack
        print("You lose. Computer has a higher score.")
    return player_won

running = True

while running:
    playing_blackjack = input("Would you like to play blackjack? (y/n): ")
    if playing_blackjack == "y":
        p_cards, c_cards = retrieve_cards()
        p_score = sum(p_cards)
        print(f"Your cards are {p_cards}, Current score: {p_score}")
        print(f"Computer's first card is {c_cards[0]}.")
        while playing_blackjack == "y":
            hit = input("Take out another card? (y/n): ")
            if hit == "y":
                add_card_to_deck(p_cards)
                p_score = sum(p_cards)
                print(f"Your cards are {p_cards}, Current score: {p_score}")
                print(f"Computer's first card is {c_cards[0]}.")
            else:
                if sum(c_cards) < 17: # Computers cards are between 1 and 16
                    while sum(c_cards) < 17: # add cards to computers deck until it's score is over or equal to 17
                        add_card_to_deck(c_cards)
                determine_a_winner(p_cards, c_cards, sum(p_cards), sum(c_cards))
                break # restart the game
    else:
        print("Thanks for playing!")
        running = False