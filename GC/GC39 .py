import random
cont = "yes"
while cont in ["yes","yeah"]:

    name = input("Who are you roasting?")
    comebacks = ["Well at least MY parents wanted me, " + name ,"Has" + name + "ever looked in a mirror?","Look who's talking","I must be blind, because I can't find who asked","do you guys hear that buzzing sound? oh it must be " + name]

    said = random.choice(comebacks)
    print(said)

    cont = input("do you want another roast?")
