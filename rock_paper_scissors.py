# import the necessaries
import random
from RPS_functions import *

# Get the game going, ask them if they want to play
print("So, you want to play Rock, Paper, Scissors?")
# ask for there response
# NB: They have to response ye ye na ye to play...
user_input=input("Ye na na ye yee? ").strip().upper()
# The whole time they want to play (ye ye na ye):
while user_input == "YE YE NA YE":
    # make the computer assign a random number between 1 and 3, to represent one of rock, paper or scissors
    computer_choice = random.randint(1,3)
    # ask them which of rock, paper, scissors they'd like to choose
    user_rps_choice = input("So then... Rock, Paper or Scissors? ").title()
    # make that choice into the corresponding number between 1 and 3, using appropriate function
    user_choice = rock_paper_scissors(user_rps_choice)
    # if they draw, tell them
    if user_choice == computer_choice:
        print("Bruh, you guys drew... Think you need to play again.")
        print(' ')
        # make them play again
        continue
    # if they lose, tell them
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        print("Bruh, you lost... Unlucky.")
        print(' ')
    # if they win, tell them
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        print("Bruh, you only went and won! GG my man.")
        print(' ')
    # if something went wrong, make them try again!
    else:
        print("Sorry, didn\'t quite catch that. Let\'s go again.")
        print(' ')
        continue
    # end of loop, ask if they want to play again?
    print("So, you want to play Rock, Paper, Scissors?")
    user_input = input("Ye na na ye yee? ").strip().upper()