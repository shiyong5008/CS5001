# NEU CS5001 Project 2 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

# main.py

# import the lib which already made in the other py file
import shapelib as s
import random

# no need watch the drawing so use tracer false
s.t.tracer(False)

# call the triangle with parameters
s.triangle(0, -250, 100, color="green", fill=True)
# call the square or box with parameters
s.square(-300, -250, 100, 100, color="green", fill=False)
# call the 5sides with parameters
s.side(300, -250, 100, color="red", fill=True)
# call the many many trees with parameters
s.forest(0, 0, 1, 100)
# call the many many snow with parameters
s.snow(-300, 200, 100, color=(random.random(), random.random(), random.random()), fill=False)

s.t.update()
s.t.mainloop()