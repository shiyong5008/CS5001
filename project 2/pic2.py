# NEU CS5001 Project 2 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

# main.py

import shapelib as s

s.t.tracer(False)

s.triangle(0, -250, 100, color="green", fill=True)
s.square(-300, -250, 100, 100, color="green", fill=False)
# s.forest(0, 0, 1, 100)
s.triangle(0, 0, 50, color="green", fill=True)
s.square(-300, 0, 50, 50, color="green", fill=False)

s.t.update()
s.t.mainloop()