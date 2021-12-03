# NEU CS5001 week8 project 11 tree.py version 4
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle_interpreter
import lsystem
import shapes
import sys

class Tree(shapes.Shape):

    """
    The init method should call the parent (Shape) init method
    with self, distance, angle, and color.
    It should assign the iterations value to an iterations field of the object (self).
    Finally, it should create an Lsystem object (passing in the filename) and assign it to an lsystem field of self.
    """
    def __init__(self, distance=5, angle=22.5, color=(0.5, 0.4, 0.3), iterations=3, filename=None):
        shapes.Shape.__init__(self, distance, angle, color)
        self.iterations = iterations
        self.lsys = lsystem.Lsystem(filename)

    """
    Given a new number of iterations in N, assign it to the iterations field of the object.
    """
    def setIterations(self, N):
        self.iterations = N

    """
    The read(self, filename) method should call the lsystem object's read method with the specified filename. 
    Use the Lsystem object you created and stored in the lsystem field to call the read method.
    """
    def read(self, filename):
        self.lsys.read(filename)

    # Override the draw method--but keep the same parameter list.
    def draw(self, xpos, ypos, scale=1.0, orientation=90):
        self.istring = self.lsys.buildString(self.iterations)
        shapes.Shape.draw(self, xpos, ypos, scale, orientation)


def main(argv):
    if len(argv) < 2:
        print('usage: %s <lsystem file 1>' % (argv[0]) )
        exit()

    tree = Tree(distance=5, angle=22.5, color="blue", iterations=4, filename=argv[1])

    tree.draw(-200, -200, 1, 90)
    tree.draw(0, -200, 1, 90)
    tree.draw(200, -200, 1, 90)

    turtle_interpreter.TurtleInterpreter().hold()

if __name__ == '__main__':
    main(sys.argv)
