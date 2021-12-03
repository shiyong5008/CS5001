# NEU CS5001 week8 project 8 growth.py version 2
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

    if len(argv) < 2:
        print( 'usage: %s <lsystem file 1>' )
        exit()

    # trees use systemFL.txt and the change of systemFLr.txt
    tree = lsystem.Lsystem( argv[1] )
    iterations = 5
    distance = 8
    angle = 30

    sx = 600
    sy = 600
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    x0 = -300
    y0 = -250

    tstr = tree.buildString( iterations )

    terp.setWidth( 2 )
    terp.setColor( (0.5, 0.4, 0.3 ) )
    terp.place( x0, y0, 90 )
    terp.drawString( tstr, distance, angle )


    tree = lsystem.Lsystem( argv[1] )
    iterations = 4
    distance = 8
    angle = 30

    sx = 600
    sy = 600
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    x0 = 0
    y0 = -250

    tstr = tree.buildString( iterations )

    terp.setWidth( 2 )
    terp.setColor( (0.5, 0.4, 0.3 ) )
    terp.place( x0, y0, 90 )
    terp.drawString( tstr, distance, angle )


    tree = lsystem.Lsystem( argv[1] )
    iterations = 3
    distance = 8
    angle = 30

    sx = 600
    sy = 600
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)

    x0 = 300
    y0 = -250

    tstr = tree.buildString( iterations )

    terp.setWidth( 2 )
    terp.setColor( (0.5, 0.4, 0.3 ) )
    terp.place( x0, y0, 90 )
    terp.drawString( tstr, distance, angle )

    terp.hold()


if __name__ == "__main__":
    main( sys.argv )
