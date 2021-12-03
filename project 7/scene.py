# NEU CS5001 week8 project 7 scene.py version 1
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle
import sys
import lsystem as ls
import turtle_interpreter as it


# draws three l-system strings given an (x,y) anchor
def nonabstract(lstr, x, y, scale, angle):
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
    if len(argv) < 3:
        print('usage: %s <lsystem filename> <lsystem filename>' % (argv[0]))
        exit()

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile(argv[1])
    # build the lsystem string with 3 iterations
    lstr = ls.buildString(lsys, 3)
    dist = float(10)
    angle = float(90)
    # draw the abstract1
    turtle.tracer(False)
    nonabstract(lstr, -100, -100, dist, angle)

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile(argv[2])
    # build the lsystem string with 3 iterations
    lstr = ls.buildString(lsys, 4)
    dist = float(3)
    angle = float(25)
    # draw the abstract2
    turtle.tracer(False)
    nonabstract(lstr, 100, -200, dist, angle)

    # wait
    it.hold()


if __name__ == "__main__":
    main(sys.argv)
