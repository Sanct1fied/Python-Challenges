healthy = 2500
totalcalories=0
user = input("start?")
while user != "end day":

    namefood = input("what did you eat?")
    caloriesfood = int(input("how many calories was in the food?"))
    while caloriesfood<1:
        print("error, please try again")
        caloriesfood = int(input("how many calories was in the food?"))



    healthy = healthy-caloriesfood

    if caloriesfood > 2500:
        print("you have eaten too much!")
    elif healthy<1:
        print("you have eaten too much!")
    else:
        print("you need to eat",healthy,"calories more")

    totalcalories = totalcalories+caloriesfood
    user = input("what would you like to do?")

if totalcalories<2000:
    print("you ate", totalcalories,"calories today. Not enough!")
elif totalcalories>2500:
    print("you ate", totalcalories,"calories today. TOO MUCH!")
else:
    print("you have eaten",totalcalories,"calories today. just right")
