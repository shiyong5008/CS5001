# NEU CS5001 Project 4 graphicsPlus drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import graphicsPlus as g
import random
def main():
    win=g.GraphWin("My window", 1000, 600)

    x=0
    y=0
    scale=1
    for i in range(30):
        cc1 = g.Circle(g.Point(x + 260 * (random.uniform(1,3)) * scale, y + 250 * (random.uniform(1,1.2)) * scale),
                       random.uniform(5,10))
        cc1.setFill("green")
        cc2 = g.Circle(g.Point(x + 260 * random.uniform(1, 2) * scale, y - 250 * random.uniform(1, 2) * scale),
                          random.uniform(10, 20))
        cc2.setFill("green")

        test4 = [cc1, cc2]

        for thing in test4:
            thing.draw(win)

        cc1.draw(win)

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()

