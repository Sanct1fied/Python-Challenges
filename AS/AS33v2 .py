import random

qs = int(input("how many questions do you want to practice?"))
hexnumber = ["a","b","c","e","f","1","2","3","4","5","6","7","8","9"]
binarynumbers = ["0","1"]

def BinaryQ():
    Binary = []
    while True:

        for i in range(8):
            binary = random.choice(binarynumbers)
            Binary.append(binary)
        print(*Binary,sep = "")

        answerB = 0
        for i in range(8,0,-1):
            answerB = answerB + (int(Binary[i-1])*(2**(8-i)))

        user_answer = int(input("what is your answer?:"))
        if user_answer == answerB:
            print("correct")
            break
        else:
            print("incorrect, the answer was" , answerB)

def HexQ():
    while True:

        Hex = []
        for i in range(2):
            hex = random.choice(hexnumber)
            Hex.append(hex)
        print(*Hex,sep = "")


        answerH = 0
        answerM = 0


        numbers = ["1","2","3","4","5","6","7","8","9"]
        letters = ["a","b","c","d","e","f"]


        if Hex[0] in letters:
            position = letters.index(Hex[0])
            answerH = position+10
            answerH = answerH * 16 ** 1
        elif Hex[0] in numbers:
            answerH = int(Hex[0])*16**1
        if Hex[1] in letters:
            position = letters.index(Hex[1])
            answerM = position+10
            answerM = answerM*16**0
        elif Hex[1] in numbers:
            answerM = int(Hex[1])*16**0
        Hextotal = answerH + answerM

        user_answer = int(input("what is your answer?:"))
        if user_answer == Hextotal:
            print("correct")
            break
        else:
            print("incorrect, the answer was" , Hextotal)
            
for i in range(qs):
    whichQ = input("what question?: binary to denary = 1, hex to denary = 2")

    if whichQ in ("2"):
        HexQ()
    elif whichQ in ("1"):
        BinaryQ()
