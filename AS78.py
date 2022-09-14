# Write your code here :-)
import turtle
import time
def face():
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(4):
            turtle.forward(100)
            turtle.right(90)

    turtle.penup()
    turtle.goto(20,-20)
    turtle.pendown()
    for i in range(4):
            turtle.forward(10)
            turtle.right(90)


    turtle.penup()
    turtle.goto(80,-20)
    turtle.pendown()
    for i in range(4):
            turtle.forward(10)
            turtle.right(90)



face()

turtle.penup()
turtle.goto(40,-80)
turtle.pendown()
turtle.left(20)
for x in range(40):
    turtle.forward(1)
    turtle.right(1)


time.sleep(3)
turtle.clear()



turtle.penup()
turtle.left(40)
face()

turtle.penup()
turtle.goto(40,-80)
turtle.pendown()
turtle.right(30)
turtle.circle(50,68)

time.sleep(3)
turtle.clear()






turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.right(37)

for i in range(4):
        turtle.forward(100)
        turtle.right(90)


turtle.penup()
turtle.goto(20,-20)
turtle.pendown()
for i in range(4):
        turtle.forward(10)
        turtle.right(90)


turtle.penup()
turtle.goto(80,-20)
turtle.pendown()
for i in range(4):
        turtle.forward(10)
        turtle.right(90)

turtle.penup()
turtle.goto(50,-90)
turtle.pendown()
turtle.right(30)
turtle.circle(10)

time.sleep(3)
turtle.clear()
