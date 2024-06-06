# rock beats scissors, scissors beats paper, paper beats rock
# program launched without arguments
# waiting for user to input rock, paper, or scissors, else say "Invalid input". input not case sensitive
# computer randomly selects rock, paper, or scissors
# program  keeps track of the score
# program prints the result of the round and asks if the user wants to play again, if invalid say invalid and wait for player to say yes or no
# if no, program prints final score and number of rounds then exits
# if yes, program continues

# import random module for computer selection
import random

# initialize variables
my_score = 0
computer_score = 0
rounds = 0
choices = ["rock", "paper", "scissors"]

# function to determine winner
def winner(user, computer):
    global my_score, computer_score, rounds
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You win!")
        my_score += 1
    else:
        print("Computer wins!")
        computer_score += 1
    rounds += 1


# main loop
while True:
    user = input("Enter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid input")
        continue
    computer = random.choice(choices)
    print(f"Computer chose {computer}")
    winner(user, computer)
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            break
        elif play_again == "no":
            print(f"Final score: You: {my_score}, Computer: {computer_score}")
            print(f"Number of rounds: {rounds}")
            exit()
        else:
            print("Invalid input")
            continue