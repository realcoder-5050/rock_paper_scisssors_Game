import random 

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("\nEnter any of them to continue rock| paper| scissors or q to quit: ")
    if user_input == "q":
        print("You quit!")
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #  rock = 0 paper = 1 scissors = 2 
    computer_picks = options[random_number]
    print(f"Computer picks {computer_picks}")

    if user_input == "paper" and computer_picks == "rock":
        print("You lost!")
        user_win += 1

    elif user_input == "rock" and computer_picks == "scissors":
        print("You lost!")
        user_win += 1

    elif user_input == "scissors" and computer_picks == "paper":
        print("You lost!")
        user_win += 1
    else:
        print("You lost!")
        computer_win += 1
print("Thanks for taking part in our game!")
print(f"You won {user_win} times")
print(f"Computer won {computer_win} times")