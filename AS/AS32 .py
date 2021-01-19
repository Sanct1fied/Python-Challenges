import random
floors = int(input("How many floors does your building have?"))

printed = []


for i in range(floors):
    number = random.randint(0,floors-1)

    while number in printed:
        number = random.randint(0,floors-1)
    if number == 0:
            print("G")
    elif number != 0:
            print(number)
    printed.append(number)
