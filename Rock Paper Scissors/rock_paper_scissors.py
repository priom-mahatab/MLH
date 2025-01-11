import random

options = ["rock", "paper", "scissors"]

choice = input("Do you want to play? (yes/no) ")
while choice.lower() == "yes":
    player_move = input("Please choose one of the following: rock, paper, scissors: ")
    while player_move.lower() not in options:
        player_move = input("Make a valid choice: ")

    computer_move = random.choice(options)

    if player_move.lower() == computer_move:
        print("Tie!")
    elif (player_move.lower() == "rock" and computer_move == "scissors") or (player_move.lower() == "paper" and computer_move == "rock") or (player_move.lower() == "scissors" and computer_move == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

    choice = input("Do you want to play again? (yes/no) ")