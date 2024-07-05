print("Welcome to the game!! ")

import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter either Rock, Paper or Scissors or Q to quit! ").lower()
    if user_input.lower() == "q":
        break

    if user_input not in options:
         continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]

    print("Computer picks",computer_pick)

    