# NEU CS5001 Project 3 Turtle drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import newshapelib as s
import sys
import random

def main():
    k = int(sys.argv[1])  # line width control at terminal input

    c="red" # control the color
    # w1=10.0 # control the line width of frame
    w2=10.0 # control the line width of signature

    s.t.tracer(False) #hides turtle tracing
    s.scene1(0, 0, k, 100)
    s.scene2(-500, -300, 1000, 600, c, False, k, w2)
    s.snow(-300, 200, 100, color=(random.random(), random.random(), random.random()), fill=False)

    s.t.update()
    s.t.mainloop()

if __name__=="__main__":
    main()
