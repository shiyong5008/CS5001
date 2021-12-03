# NEU CS5001 Project 1 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

# shapes.py

from turtle import *

def triangle(length1,c1): # draw triangle with equal length1
    color(c1)
    forward(length1)
    left(120)
    forward(length1)
    left(120)
    forward(length1)
    left(120)

    up()
    backward(200)
    down()

def square(length2,c2): # draw square with equal length2
    color(c2)
    forward(length2)
    left(90)
    forward(length2)
    left(90)
    forward(length2)
    left(90)
    forward(length2)
    left(90)

    up()
    backward(200)
    down()

def sides(length3,c3): # draw 6sides with equal length3
    color(c3)
    forward(length3)
    left(60)
    forward(length3)
    left(60)
    forward(length3)
    left(60)
    forward(length3)
    left(60)
    forward(length3)
    left(60)
    forward(length3)
    left(60)

    up()
    forward(400)
    left(90)
    forward(200)
    right(90)
    down()

tracer(False)

def test(length1,c1,length2,c2,length3,c3):
    triangle(length1,c1) #call the triangle
    square(length2,c2) #call the square
    sides(length3,c3) #call the 6sides

test(100, "red", 100, "blue", 100, "yellow")
test(50, "red", 50, "blue", 50, "yellow")

def house(length1,c1,length2,c2):
    up()
    forward(400)
    right(90)
    forward(200)
    left(90)
    down()

    triangle(length1, c1)  # call the triangle
    up()
    forward(210)
    right(90)
    forward(80)
    left(90)
    down()

    square(length2, c2)  # call the square

house(100,"pink",80,"red")


mainloop()