###060
##import turtle
##for i in range(0,4):
##    turtle.right(90)
##    turtle.forward(100)
##turtle.exitonclick()
##
###061
##import turtle
##for i in range(0,3):
##    turtle.forward(90)
##    turtle.left(120)
##turtle.exitonclick()
##
###062
##import turtle
##for i in range(0,360):
##    turtle.forward(1)
##    turtle.right(1)
##turtle.exitonclick()
##
###063
##import turtle
##turtle.begin_fill()
##turtle.color("black","green")
##for i in range(0,4):
##    turtle.forward(90)
##    turtle.right(90)
##turtle.end_fill()
##turtle.penup()
##turtle.forward(100)
##turtle.pendown()
##turtle.begin_fill()
##turtle.color("black","white")
##for i in range(0,4):
##    turtle.forward(90)
##    turtle.right(90)
##turtle.end_fill()
##turtle.penup()
##turtle.forward(100)
##turtle.pendown()
##turtle.begin_fill()
##turtle.color("black","orange")
##for i in range(0,4):
##    turtle.forward(90)
##    turtle.right(90)
##turtle.end_fill()
##turtle.exitonclick()
##
###064
##import turtle
##for i in range(0,5):
##    turtle.forward(90)
##    turtle.left(144)
##turtle.exitonclick()
##
###065
##import turtle
###number1
##turtle.left(90)
##turtle.forward(100)
##turtle.penup()
###number2
##turtle.right(90)
##turtle.forward(20)
##turtle.pendown()
##turtle.forward(100)
##turtle.right(90)
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(100)
##turtle.left(90)
##turtle.forward(50)
##turtle.left(90)
##turtle.forward(100)
##turtle.penup()
###number3
##turtle.forward(20)
##turtle.pendown()
##turtle.forward(100)
##turtle.left(90)
##turtle.forward(50)
##turtle.left(90)
##turtle.forward(75)
##turtle.backward(75)
##turtle.right(90)
##turtle.forward(50)
##turtle.left(90)
##turtle.forward(100)
##turtle.hideturtle()
##turtle.exitonclick()
##
###066
##import turtle
##import random
##turtle.pensize(3)
##for i in range(0,8):
##    turtle.color(random.choice(["red","orange","yellow","green","blue","purple"]))
##    turtle.forward(90)
##    turtle.left(45)
##turtle.exitonclick()
##
###067
##import turtle
##for i in range(0,10):
##    turtle.left(36)
##    for i in range(0,8):
##        turtle.forward(35)
##        turtle.left(45)
##turtle.hideturtle()
##turtle.exitonclick()

#068
import turtle
import random
lines = random.randint(5,20)
length = random.randint(20,100)
angle = random.randint(1,365)
for i in range(0,lines):
    turtle.left(angle)
    turtle.forward(length)
turtle.hideturtle()
turtle.exitonclick()
