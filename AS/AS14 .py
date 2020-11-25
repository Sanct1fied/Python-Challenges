equation = str(input("What is your equation?:"))
equation = [char for char in equation]
leftbracket = ["("]
rightbracket = [")"]
totalleft = 0
totalright = 0
num = len(equation)
for i in range(num):
    if equation[i] in leftbracket:
        totalleft = totalleft+1
    elif equation[i] in rightbracket:
        totalright = totalright+1

if totalleft == totalright:
    print("you have a balanced number of brackets in your equation")
else:
    print("you have a unbalanced number of brackets in your equation")
    
if totalleft<totalright:
    totalright = totalright-totalleft
    print("you have", totalright, "more right brackets than left")
elif totalleft>totalright:
    totalleft = totalleft-totalright
    print("you have", totalleft,"more left brackets than right")
