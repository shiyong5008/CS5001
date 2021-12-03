# Yong Shi extension
# test function for project 9 task2 Create three more shape classe

import turtle_interpreter
import shapes
import tree

# a simple test function that draws squares and triangles
def main():

    # create a square object and draw a bunch of them
    s = shapes.Square()
    s.setColor( (0.3, 0.2, 0.9) )
    for i in range(36):
        s.draw(0, -100, scale=0.75, orientation=i*10)

    # create a triangle object and draw a bunch of them
    t = shapes.Triangle()
    t.setColor( (0.8, 0.2, 0.3) )
    for i in range(20):
        t.draw(0, 100, scale=0.8, orientation=i*18)

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

    # wait
    turtle_interpreter.TurtleInterpreter().hold()


if __name__ == '__main__':
    main()

