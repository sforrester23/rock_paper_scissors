import random
from RPS_functions import *

print("So, you want to play Rock, Paper, Scissors?")
user_input=input("Ye na na ye yee? ").strip().upper()
while user_input == "YE YE NA YE":
    computer_choice = random.randint(1,3)
    user_rps_choice = input("So then... Rock, Paper or Scissors? ").title()
    user_choice = rock_paper_scissors(user_rps_choice)
    if user_choice == computer_choice:
        print("Bruh, you guys drew... Think you need to play again.")
        print(' ')
        continue
    elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
        print("Bruh, you lost... Unlucky.")
        print(' ')
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        print("Bruh, you only went and won! GG my man.")
        print(' ')
    else:
        print("Sorry, didn\'t quite catch that. Let\'s go again.")
        print(' ')
        continue
    print("So, you want to play Rock, Paper, Scissors?")
    user_input = input("Ye na na ye yee? ").strip().upper()