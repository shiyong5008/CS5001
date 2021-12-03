# NEU CS5001 Project 3 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845


import newshapelib as s

s.t.tracer(False)

# call the scene1 and scene2
s.scene1(0, 0, 1, 100)
s.scene2(-500, -300, 1000, 600, "black", False, 2.0, 10.0)

s.t.update()
s.t.mainloop()