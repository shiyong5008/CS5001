# NEU CS5001 week8 project 7 grid.py version 1
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle
import sys
import lsystem as ls
import turtle_interpreter as it


# draws grid l-system strings given a lsystem, (x,y) anchor, scale
def grid(key, x, y, scale):

    # create the lsystem from a file
    lsys = ls.createLsystemFromFile(key)
    # build the lsystem string with i iterations
    for i in range(3):
        lstr = ls.buildString(lsys, i+1)
        for j in [22,46,60]:
            angle = float(j)

            oldheading = turtle.heading()

            turtle.up()
            turtle.goto(x, y)
            turtle.down()
            turtle.right(270)
            turtle.color(0.5, 0.6, 0.8)
            turtle.width(2)

            it.drawString(lstr, scale * 0.75, angle)

            turtle.setheading(oldheading)

            y=y-scale*30
        y=y+scale*90
        x=x+scale*30

    return

# takes in the list of strings from the command line
# reads in an lsystem file, generates the string
def main(argv):

    # check if there are enough arguments
    if len(argv) < 2:
        print('usage: %s <lsystem filename>' % (argv[0]))
        exit()


    # draw the abstract1
    turtle.tracer(False)
    grid(argv[1], -200, 100, 5)

    # wait
    it.hold()


if __name__ == "__main__":
    main( sys.argv )