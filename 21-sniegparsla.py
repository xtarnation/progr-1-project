import turtle
##snow = turtle.Turtle()

##for i in range(4):
##    snow.forward(100)
##    snow.right(90)


##import random
##turtle.Screen().bgcolor("black")
##colors = ["green", "cyan", "blue", "white"]
##snow.color("black")
##for i in range(10):
##    for i in range(2):
##        snow.forward(100)
##        snow.right(60)
##        snow.forward(100)
##        snow.right(120)
##    snow.right(36)
##    snow.color(random.choice(colors))


##snow.penup()
##snow.forward(90)
##snow.left(45)
##snow.pendown()
##
##def branch():
##    for i in range(3):
##        for i in range(3):
##            snow.forward(30)
##            snow.backward(30)
##            snow.right(45)
##        snow.left(90)
##        snow.backward(30)
##        snow.left(45)
##    snow.right(90)
##    snow.forward(90)
##
##for i in range(8):
##    branch()
##    snow.left(45)


flake = turtle.Turtle()
turtle.Screen().bgcolor("grey")
flake.color("white")
def snowflake():
    for i in range(3):
        for i in range(3):
            flake.forward(15)
            flake.backward(15)
            flake.right(45)
        flake.left(90)
        flake.backward(30)
        flake.left(45)
    flake.right(75)
    flake.forward(90)

for i in range(12):
    snowflake()
    flake.left(45)




