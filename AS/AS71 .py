import random
import time
digits = int(input("how many digits is the passcode?:"))
password = ""
for i in range(digits):
    password1 = random.randint(0,9)

    password = password + str(password1)

correct = 0
passed = 0
print("cracking in")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
while correct != int(password):
    correct = correct+1



print("password is:",correct,)
