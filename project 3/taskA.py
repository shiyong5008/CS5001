# NEU CS5001 Project 3 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845


import newshapelib as s

s.t.tracer(False)

for i in range(3):
    s.triangle(0+i*100, -250+i*100, 100+i*100, color="green", fill=True)

s.t.update()
s.t.mainloop()