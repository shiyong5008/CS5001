# NEU CS5001 week8 project 8 arrangement.py version 2
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import sys
import turtle_interpreter
import lsystem

def main(argv):
    """ Draw a single tree, using an Lsystem and the TurtleInterpeter
    This progarm expects the name of an L-system file, the number of iterations
    to use to generate the tree string, the distance associated with F, and
    the angle.
    """

    if len(argv) < 3:
        print( 'usage: %s <lsystem file 1> <lsystem file 2>' )
        exit()

    # tree1 use systemFL.txt
    tree = lsystem.Lsystem( argv[1] )
    iterations = 5
    distance = 8
    angle = 25

    sx = 600
    sy = 600
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    x0 = -200
    y0 = -250

    tstr = tree.buildString( iterations )

    terp.setWidth( 2 )
    terp.setColor( (0.5, 0.4, 0.3 ) )
    terp.place( x0, y0, 90 )
    terp.drawString( tstr, distance, angle )

    # tree2 use systemGL.txt
    tree = lsystem.Lsystem( argv[2] )
    iterations = 8
    distance = 8
    angle = 30

    sx = 600
    sy = 600
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    x0 = 200
    y0 = -250

    tstr = tree.buildString( iterations )

    terp.setWidth( 2 )
    terp.setColor( (0.5, 0.4, 0.3 ) )
    terp.place( x0, y0, 90 )
    terp.drawString( tstr, distance, angle )

    terp.hold()


if __name__ == "__main__":
    main( sys.argv )
