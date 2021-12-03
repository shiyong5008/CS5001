# NEU CS5001 week8 project 11 scene3
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle_interpreter
import shapes
import random

#define the 3 kinds of shapes in a tile from square and five side and side yellow
def tile(x, y, scale):
    # use random colors
    color1 = (random.random(), random.random(), random.random())
    color2 = (random.random(), random.random(), random.random())
    color3 = (random.random(), random.random(), random.random())

    # draw the square
    s = shapes.Square()
    s.setColor( color1 )
    s.setWidth( 1 )
    s.setStyle( 'jitter3' )
    s.setJitter( 2 )
    s.draw(x, y, scale/100, orientation=90)

    #draw the fiveSide
    fS=shapes.fiveSide()
    fS.setColor( color2 )
    fS.draw(x+scale, y+scale, scale/100, orientation=90)

    #draw the SideYellow
    SY=shapes.SideYellow()
    SY.setColor( color3 )
    SY.draw(x-scale, y+scale, scale/100, orientation=90)

# call the function and draw a loop of shapes with 5X5.
def mosaic(x, y, scale, Nx, Ny):
    for i in range(Nx):
        for j in range(Ny):
            tile(x+100*i,y-100*j,scale)
    # wait
    turtle_interpreter.TurtleInterpreter().hold()

def main():
    mosaic(-300,100,50,5,5)

if __name__ == '__main__':
    main()
