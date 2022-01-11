import time

siblings = int(input("how many siblings are there?:"))
total_time = int(input("How much time do we have (Hours)?:"))
timeleft = 0

time_per_sibling = total_time/siblings
print("there is", time_per_sibling, "hours per sibling")

start = input("Start timer?")
