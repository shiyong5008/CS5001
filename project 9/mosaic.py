# NEU CS5001 week8 project 9 mosaic.py version 3
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle_interpreter
import lsystem
import shapes
import sys
import tree
import random

def tile(x, y, scale):
    color1 = (random.random(), random.random(), random.random())
    color2 = (random.random(), random.random(), random.random())
    color3 = (random.random(), random.random(), random.random())
    s = shapes.Square()
    s.setColor( color1 )
    s.draw(x, y, scale/100, orientation=90)
    fS=shapes.fiveSide()
    fS.setColor( color2 )
    fS.draw(x+scale, y+scale, scale/100, orientation=90)
    SY=shapes.SideYellow()
    SY.setColor( color3 )
    SY.draw(x-scale, y+scale, scale/100, orientation=90)

def mosaic(x, y, scale, Nx, Ny):
    for i in range(Nx):
        for j in range(Ny):
            tile(x+100*i,y-100*j,scale)
    # wait
    turtle_interpreter.TurtleInterpreter().hold()

def main():
    mosaic(-300,100,20,5,4)

if __name__ == '__main__':
    main()
