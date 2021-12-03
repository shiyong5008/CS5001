# NEU CS5001 week8 project 9 place.py version 3
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle_interpreter
import lsystem
import shapes
import sys
import tree

# a simple test function that draws shapes and trees
def main(argv):

    # create a tree object and draw 3 of them with systemH.txt
    if len(argv) < 2:
        print('usage: %s <lsystem file 1>' % (argv[0]) )
        exit()
    tr = tree.Tree(distance=5, angle=22.5, color="olive", iterations=5, filename=argv[1])
    tr.draw(-100, -200, 1, 90)
    tr.draw(0, -200, 1, 90)
    tr.draw(100, -200, 1, 90)

    # create a fillTriangle object and draw a bunch of them
    fT=shapes.fillTriangle()
    fT.setColor( (0.8, 0.2, 0.3) )
    for i in range(20):
        fT.draw(250, -100, scale=0.75, orientation=i*30)

    # create a 5sides object and draw it
    fS=shapes.fiveSide()
    fS.setColor( "red" )
    fS.draw(-300, -50, scale=0.75, orientation=0)

    # create a star object and draw a red one
    S=shapes.Side()
    S.setColor( "red" )
    S.draw(-300, 200, scale=0.75, orientation=0)

    # create a star object and draw a yellow one
    SY=shapes.SideYellow()
    SY.setColor( "yellow" )
    SY.draw(200, 200, scale=0.75, orientation=0)

    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == '__main__':
    main(sys.argv)
