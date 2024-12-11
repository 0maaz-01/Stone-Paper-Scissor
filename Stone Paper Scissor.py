import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player=input(("Enter rock, paper or scissors: ")).lower()

    if computer== player:
        print("computer:", computer)
        print(("player:", player))
        print("Tie")

    elif computer == "rock":
        if player== "paper":
            print("computer:",computer)
            print("player:", player)
            print("You Won!")
        if player== "scissors":
            print("computer:",computer)
            print("player:", player)
            print("You Lost!")

    elif computer == "paper":
        if player== "scissors":
            print("computer:",computer)
            print("player:", player)
            print("You Won!")
        if player== "rock":
            print("computer:",computer)
            print("player:", player)
            print("You Lost!")

    elif computer == "scissors":
        if player== "rock":
            print("computer:",computer)
            print("player:", player)
            print("You Won!")
        if player== "paper":
            print("computer:",computer)
            print("player:", player)
            print("You Lost!")



    play_again = input("Play again? (yes/no): ").lower()

    if play_again!= "yes":
        break

print("Bye!")