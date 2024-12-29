# stone paper scissors game.

import random
input_of_game = ["stone","paper","scissors"]
def welcome():
    print("Welcome To Stone Paper Scissors Game!!")
    print("Instructions:")
    print("1. You will play against the computer.")
    print("2. You can choose one of the following options: 'stone', 'paper', or 'scissors'.")
    print("3. Stone beats Scissors.")
    print("4. Scissors beats Paper.")
    print("5. Paper beats Stone.")
    print("6. If you and the computer choose the same option, it's a tie.")
    print("Let's begin the game!\n")

def user_choice():
    while True:
        user_input=input("Enter the choice(stone,paper,scissors):").lower()
        if user_input in input_of_game:
            return user_input
        else:
            print("please choose valid input.")

def comparison(user_input,computer_input):
    if user_input== computer_input:
        print("It's a tie!!")
    elif (user_input=="stone" and computer_input=="scissors"
          or user_input=="paper" and computer_input=="stone"
          or user_input=="scissors" and computer_input=="paper"):
        print(f"User takes {user_input} and computer takes {computer_input}.{user_input} beats {computer_input} and user wins.")
    else:
        print("Computer wins.")

def play_game():
    welcome()
    while True: 
        user_input=user_choice()
        print(f"user chose :{user_input}")
        computer_input=random.choice(input_of_game)
        print(f"Computer chose:{computer_input}")
        comparison(user_input,computer_input)
        play_again=input("Do you want to play again(y/n)?").lower()
        if play_again=='y':
            continue
        else:
            print("You have ended the game.")
            break
    print("See you next time!")
play_game()








