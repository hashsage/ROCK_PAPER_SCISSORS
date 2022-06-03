import random

while True:
    user_action = input("Enter a choice (R, P or S): ")
    possible_actions = ["R", "P", "s"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        if user_action == "R":
            print("Player(Rock) : CPU(Rock)")
        elif user_action == "P":
            print("Player(Paper) : CPU(Paper)")
        elif user_action == "S":
            print("Player(Scissors) : CPU(Scissors)")
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "R":
        if computer_action == "S":
            print("Player(Rock) : CPU(Scissors)")
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Player(Rock) : CPU(Paper)")
            print("Paper covers rock! You lose.")
            break
    elif user_action == "P":
        if computer_action == "R":
            print("Player(Paper) : CPU(Rock)")
            print("Paper covers rock! You win!")
            break
        else:
            print("Player(Paper) : CPU(Scissors)")
            print("Scissors cuts paper! You lose.")
            break
    elif user_action == "S":
        if computer_action == "P":
            print("Player(Scissors) : CPU(Paper)")
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Player(Scissors) : CPU(Rock)")
            print("Rock smashes scissors! You lose.")
            break
    elif (user_action != "R" or user_action != "P" or user_action != "S") :
    	print("Invalid input! please try again")
