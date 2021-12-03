# NEU CS5001 week8 project 7 extension1.py version 1
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle
import sys
import lsystem as ls
import turtle_interpreter as it


# draws three l-system strings given an (x,y) anchor
def abstract(lstr, x, y, scale, angle, color, k):
    oldheading = turtle.heading()

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.right(k)
    turtle.color(color)
    turtle.width(2)
    it.drawString(lstr, scale * 0.75, angle)

    turtle.setheading(oldheading)

    return

# takes in the list of strings from the command line
# reads in an lsystem file, generates the string
def main(argv):

    # check if there are enough arguments
    if len(argv) < 2:
        print('usage: %s <lsystem filename>' % (argv[0]))
        exit()

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile(argv[1])
    # build the lsystem string with 3 iterations
    lstr = ls.buildString(lsys, 3)
    dist = float(5)
    angle = float(25)
    # draw the abstract1
    turtle.tracer(False)
    abstract(lstr, -200, 100, dist, angle, "red", 0)
    abstract(lstr, -200, 100, dist, angle, "yellow", 90)
    abstract(lstr, -200, 100, dist, angle, "blue", 180)
    abstract(lstr, -200, 100, dist, angle, "green", 270)


    # wait
    it.hold()


if __name__ == "__main__":
    main(sys.argv)
