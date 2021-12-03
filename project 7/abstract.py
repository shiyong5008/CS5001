# NEU CS5001 week8 project 7 abstract.py version 1
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle
import sys
import lsystem as ls
import turtle_interpreter as it


# draws three l-system strings given an (x,y) anchor
def abstract(lstr, x, y, scale, angle):
    oldheading = turtle.heading()

    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.right(270)
    turtle.color(0.5, 0.6, 0.8)
    turtle.width(2)
    it.drawString(lstr, scale * 0.75, angle)

    turtle.setheading(oldheading)

    return

# takes in the list of strings from the command line
# reads in an lsystem file, generates the string
def main(argv):

    # check if there are enough arguments
    if len(argv) < 4:
        print('usage: %s <lsystem filename> <lsystem filename> <lsystem filename>' % (argv[0]))
        exit()

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile(argv[1])
    # build the lsystem string with 3 iterations
    lstr = ls.buildString(lsys, 3)
    dist = float(10)
    angle = float(90)
    # draw the abstract1
    turtle.tracer(False)
    abstract(lstr, -200, 100, dist, angle)

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile(argv[2])
    # build the lsystem string with 3 iterations
    lstr = ls.buildString(lsys, 3)
    dist = float(5)
    angle = float(90)
    # draw the abstract2
    turtle.tracer(False)
    abstract(lstr, 50, 50, dist, angle)

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile(argv[3])
    # build the lsystem string with 3 iterations
    lstr = ls.buildString(lsys, 3)
    dist = float(5)
    angle = float(25)
    # draw the abstract3
    turtle.tracer(False)
    abstract(lstr, -100, -250, dist, angle)

    # wait
    it.hold()


if __name__ == "__main__":
    main(sys.argv)
