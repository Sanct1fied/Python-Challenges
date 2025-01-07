import random
import time
print("welcome to the parity bit checker quiz!")
time.sleep(1)


def paritybitchecker(parity):
    bit = []
    totalones = 0

    answer = ""
    for i in range(7):
        byte = random.randint(0,1)
        bit.append(byte)
        print(bit)
    num = len(bit)
    for i in range(num):
        if bit[i] == 1:
            totalones += 1
        else:
            pass
    if parity == "odd":
        if totalones in [0,2,4,6,8]:
            answer = "1"
        if totalones in [1,3,5,7]:
            answer = "0"

    if parity== "even":
        if totalones in [0, 2, 4, 6, 8]:
            answer = "0"
        if totalones in [1, 3, 5, 7]:
            answer = "1"
    print("the parity is:", parity)
    useranswer = input("what is your answer?")
    if useranswer == answer:
        print("correct")
    else:
        print("wrong. the correct answer is:", answer)

true = 1
while true == 1 :
    anotherquestion = input("would you like to practice another? Y/N")
    if anotherquestion in ["Y"]:
        parity = random.choice(["even", "odd"])
        paritybitchecker(parity)
    elif anotherquestion in ["N"]:
        print("thank you for playing!")
        time.sleep(2)
        true = 0
    else:
        print("sorry I can only accepy Y/N")
        pass
