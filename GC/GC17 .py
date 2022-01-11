ISBN = input("please input your ISBN number:")
while len(ISBN) != 9:
    ISBN = input("must be 9 numbers:")
num1 = int(ISBN[0])
num2 = int(ISBN[1])
num3 = int(ISBN[2])
num4 = int(ISBN[3])
num5 = int(ISBN[4])
num6 = int(ISBN[5])
num7 = int(ISBN[6])
num8 = int(ISBN[7])
num9 = int(ISBN[8])
multiplied1 = (num1*10)
multiplied2 = (num2*9)
multiplied3 = (num3*8)
multiplied4 = (num4*7)
multiplied5 = (num5*6)
multiplied6 = (num6*5)
multiplied7 = (num7*4)
multiplied8 = (num8*3)
multiplied9 = (num9*2)
allnum = (multiplied1+multiplied2+multiplied3+multiplied4+multiplied5+multiplied6+multiplied7+multiplied8+multiplied9)
modulo = allnum%11
finalnumber = 11-modulo

if finalnumber == 10:
    print("the check digit is X")
elif finalnumber == 11:
    print("the check digit is 0")
else:
    print("the check digit is", finalnumber)
