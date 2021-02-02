import turtle
turtle.speed(6)

turtle.penup()
turtle.right(180)
turtle.fd(500)
turtle.left(180)
turtle.pendown()
turtle.left(45)



def drawtree(lineRlen, lineLen ):

    for i in range(5):


        turtle.fd(lineLen)
        turtle.right(225)
        turtle.fd(lineRlen)
        turtle.left(225)
        lineLen = lineLen-10
        lineRlen = lineRlen - 10
        print(lineLen)
        print(lineRlen)

    turtle.fd(50)

def drawtreedown(lineRlen, lineLen ):

    for i in range(5):


        turtle.fd(lineLen)
        turtle.left(225)
        turtle.fd(lineRlen)
        turtle.right(225)
        lineLen = lineLen+10
        lineRlen = lineRlen + 10

    turtle.fd(50)

drawtree(50,100)

turtle.right(90)

drawtreedown(10,50)

turtle.fd(50)
turtle.left(225)
turtle.fd(142)
turtle.left(90)
turtle.fd(100)
turtle.right(90)
turtle.fd(50)
turtle.right(90)
turtle.fd(100)
turtle.left(90)
turtle.fd(142)
