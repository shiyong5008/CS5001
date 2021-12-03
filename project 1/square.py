# NEU CS5001 Project 1 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

# shapes.py

from turtle import *

def scene2(length2,c2): # draw square with equal length2
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

scene2(100,"blue") #call the square with 100 and blue
mainloop()