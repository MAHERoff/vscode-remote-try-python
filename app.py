#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

def get_user_choice():
    user_input = input("Choose rock, paper, or scissors: ").lower()
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_input = input("Choose again: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "You win!", 1
    else:
        return "You lose!", -1

def play_game():
    user_wins = 0
    total_rounds = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice}. Computer chose {computer_choice}.")

        result, points = determine_winner(user_choice, computer_choice)
        print(result)

        if points == 1:
            user_wins += 1
        elif points == -1:
            total_rounds += 1

        print(f"Score - You: {user_wins} Computer: {total_rounds}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Final Score - You: {user_wins} Computer: {total_rounds}")
            if user_wins > total_rounds:
                print("Well done, you are the best!")
            else:
                print("Game over.")
            break

if __name__ == "__main__":
    play_game()