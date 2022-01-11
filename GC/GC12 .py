import time
continued = 1

while continued == 1:
    siblings = int(input("how many siblings are there?:"))
    total_time = int(input("How much time do we have (Hours)?:"))
    total_minutes = total_time*60
    timeleft = 0

    time_per_sibling = total_minutes/siblings
    print("there is", time_per_sibling, "minutes per sibling")
    siblings_left = siblings

    while siblings_left > 0:
        start = input("Start timer?")
        if start in ["yes"]:
            time_per_sibling = total_minutes/siblings
            for i in range(int(time_per_sibling)):
                print(time_per_sibling-i)
                time.sleep(0.1)
            print("TIME IS UP")
            siblings_left -= 1

    print("all the siblings should've had their turn")
    continued = input("input '0' to stop")

