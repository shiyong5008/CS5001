# NEU CS5001 Project 1 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

# shapes.py

from turtle import *

def test(length1, others):
    color(others)
    forward(length1)
    left(120)
    forward(length1)
    left(120)
    forward(length1)
    left(120)

test(100, "red")

mainloop()