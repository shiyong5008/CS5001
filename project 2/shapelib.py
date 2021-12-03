# NEU CS5001 Project 2 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

# shapelib.py

# import turtle as t and import random
import turtle as t
import random

# goto function puts the t at (x, y)
def goto(x, y):
    t.up()
    t.goto(x, y)
    t.down()

# square function draws at (x, y) with size (width, height)
def square(x, y, width, height, color="green", fill=False):
    goto(x, y)
    t.color(color)
    if fill:
        t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    if fill:
        t.end_fill()

# triangle function draws at (x, y) with size (length)
def triangle(x, y, length, color="green", fill=True):
    goto(x, y)
    t.color(color)
    if fill:
        t.begin_fill()
    for i in range(3):
        t.forward(length)
        t.left(120)
    if fill:
        t.end_fill()

# 5 side objective function draws at (x, y) with size (length)
def side(x, y, length, color="red", fill=True):
    goto(x, y)
    t.color(color)
    if fill:
        t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.left(72)
    if fill:
        t.end_fill()

# tree function with triangle on top of square
def tree(x, y, size, color):
    square(x, y, size, size*10, color, False)
    triangle(x-size*2, y+size*10, size*5, color, True)

# turn off turtle tracing
# t.tracer(False)

# draw many many trees with random
def forest(x, y, size, n):
    for i in range(n):
        tree(x+i*10*random.uniform(-0.5,0.5),
            y-100+300*random.uniform(0,0.5),
            size*i*random.uniform(0,0.1),
            (random.random(), random.random(), random.random()))

# draw many many snow with random
def snow(x, y, length, color, fill=False):
    for j in range(100):
        goto(x+random.uniform(-300,900), y+random.uniform(0,100))
        color=(random.random(), random.random(), random.random())
        length=random.uniform(10,30)
        t.color(color)
        if fill:
            t.begin_fill()
        for i in range(30):
            t.forward(length)
            t.left(120)
            t.left(30)

            t.end_fill()

# below was test using so for the lib file remove the output code
# t.tracer(False)
# forest(0, 0, 1, 100)

# t.update()
# t.mainloop()



