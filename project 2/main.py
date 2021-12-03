# NEU CS5001 Project 2 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

# main.py

# import the lib which already made in the other py file
import shapelib as s

# pop up pic at same time, no need watch the drawing
s.t.tracer(False)

# call many many trees which the parameters
s.forest(0, 0, 1, 100)

s.t.update()
s.t.mainloop()