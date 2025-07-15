print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island. Your mission is to find the treasure.\nYou are currently stranded in the middle of nowhere in the state of Florida.")
first_path = input("Which road do you take? 'left' or 'right'\n").lower()
game_over = False
if first_path == "left":
    print("The road took you to a Big Mansion, you arrived outside the gate.")
    second_path = input("You have two options to choose from:\n1. Jump the gate and run towards the entrance\n2. Walk down a road towards the left.\n")
    if second_path == "1":
        third_path = input("You made it to the entrance of the Mansion. You have three doors to go through.\n1. A black Door With a raven etched into it.\n2. The Biggest Door with water leaking from underneath it.\n3. An ancient green door with green moss growing on it\n")
        if third_path == "1":
            game_over = True
            print("You walked into the dark empty room and the door slammed shut. Immediately hundreds of locks and chains surrounded the door with no escape.")
        elif third_path == "2":
            game_over = True
            print("You pushed the big door open, walking through the water everything seemed fine until you notice something big breathing under a blanket. You walked towards the blanket lifting it up only to realize you were stepping in the giant tiger's drool. Dinner was ready but not for you.")
        elif third_path == "3":
            print("You chose the ancient green door. You walked into the wooded room. Turning on the lights with a pull chain. You spot a small chest with a bluish purplish aura. You open the chest to find Diamonds and Amethyst! WE'RE RICH! (We're?)")
        else:
            game_over = True
            print("No door was chosen. You decided to get inside through a window and got shot. You were taken to a hospital and survived the wound. The homeowners upped there security.")
    elif second_path == "2":
        print("As you walked further and further down the road it got stepper and stepper leading you with no other options but to keep going. You made it towards the end with no way up. There was nothing down there.")
        game_over = True
else:
    game_over = True
    print("As you went deeper and deeper down this road it got more and more treacherous.\nYou were chased down and eaten by Alligators.")

if game_over:
    print("GAME OVER!")
else:
    print("YOU WIN!")