# NEU CS5001 week8 project 11 scene2.py
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle_interpreter
import shapes

# set function to draw a series of shapes like tree to pile up
def tree( element, x, y, scale ):
    if scale<10:
        return
    element.draw(x,y,scale)
    tree(element,  x - 0.4*scale, y + 0.5*scale, scale*0.5)
    tree(element, x + scale*0.9, y + 0.5 * scale, scale * 0.5)

def main():
    # call the triangle as the element to draw tree with calling the tree function
    s = shapes.Triangle( distance=1, color='red' )
    s.setWidth( 3 )
    s.setStyle( 'normal' )
    s.setJitter( 0 )
    tree( s, 150, -150, 100)

    # call the triangle as the element to draw tree with calling the tree function
    s = shapes.Triangle( distance=1, color='blue' )
    s.setWidth( 2 )
    s.setStyle( 'jitter' )
    s.setJitter( 2 )
    tree( s, 150, 150, 100)

    # define two strings
    square = 'F-F-F-F-'
    triangle = 'F-F-F-'

    terp = turtle_interpreter.TurtleInterpreter()

    # draw normal
    terp.place(-200, 300)
    terp.setStyle('normal')
    terp.setColor("blue")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    # draw jitter
    terp.place(-200, 150)
    terp.setStyle('jitter')
    terp.setJitter(2)
    terp.setColor("red")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    # draw jitter3
    terp.place(-200, 0)
    terp.setStyle('jitter3')
    terp.setJitter(2)
    terp.setColor("blue")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    # draw dotted
    terp.place(-200, -150)
    terp.setStyle('dotted')
    terp.setJitter(2)
    terp.setColor("")
    terp.setWidth(1)
    terp.drawString(square, 100, 90)

    terp.hold()


if __name__ == "__main__":
    main()
