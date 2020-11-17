import random

play = "yes"

while play in ["yes","Yes","YES"]:
    player = input("\nRock, Paper Or Scissors?:")
    friend = ["I chose Rock","I chose Paper","I chose Scissors"]
    friendsaid = random.choice(friend)
    if player in ["Rock", "rock"]:
        print(friendsaid)
        if friendsaid in ["I chose Rock"]:
            print("Draw!")
        elif friendsaid in ["I chose Scissors"]:
            print("You Won")
        else:
            print("You Lost")
    if player in ["Paper", "paper"]:
        print(friendsaid)
        if friendsaid in ["I chose Paper"]:
            print("Draw!")
        elif friendsaid in ["I chose Rock"]:
            print("You Won!")
        else:
            print("You Lost")
    if player in ["Scissors", "scissors"]:
        print(friendsaid)
        if friendsaid in ["I chose Scissors"]:
            print("Draw!")
        elif friendsaid in ["I chose Paper"]:
            print("You Won!")
        else:
            print("You Lost")
    play = input("\ndo you wanna play again?:")

