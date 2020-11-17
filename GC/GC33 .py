play = "yes"

while play in ["yes","Yes","YES"]:
    speech = input("\nDo you confess?:")
    friend = ["Your friend was silent","Your friend confessed"]
    friendsaid = random.choice(friend)
    if speech in ["no","No","NO"]:
        print(friendsaid)
        if friendsaid in ["Your friend was silent"]:
            print("you both spend 5 years in prison")
        else:
            print("You will spend 20 years in prison to answer for your crimes")
    if speech in ["yes","Yes","YES"]:
        print(friendsaid)
        if friendsaid in ["Your friend was silent"]:
            print("You condemned your friend to 20 years in prison")
        else:
            print("You both will spend 5 years in prison")
    play = input("\ndo you wanna play again?:")
