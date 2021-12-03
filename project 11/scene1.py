# NEU CS5001 week8 project 11 scene1.py
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845


import shapes

# set function to draw a series of shapes over and over up
def drawStack( element, x, y, scale ):
    if scale<20:
        return
    element.draw(x,y,scale)
    drawStack(element, x + scale*0.1, y + scale*0.8, scale*0.8)
    return

# set function to draw a series of shapes like tree to pile up
def tree( element, x, y, scale ):
    if scale<10:
        return
    element.draw(x,y,scale)
    tree(element,  x - 0.4*scale, y + 0.5*scale, scale*0.5)
    tree(element, x + scale*0.9, y + 0.5 * scale, scale * 0.5)


def main():

# call the square as the element to draw tree with calling the tree function
    s = shapes.Square( distance=1, color='green' )
    s.setWidth( 1 )
    s.setStyle( 'normal' )
    s.setJitter( 0 )
    tree( s, -250, -150, 100)

# call the square as the element to draw stack with calling the stack function
    s = shapes.Square( distance=1, color='purple' )
    s.setWidth( 3 )
    s.setStyle( 'jitter' )
    s.setJitter( 3 )
    drawStack(s, 200, -150, 100)

# call the triangle as the element to draw stack with calling the stack function
    s = shapes.Triangle( distance=1, color='blue' )
    s.setWidth( 1 )
    s.setStyle( 'jitter3' )
    s.setJitter( 2 )
    drawStack(s, 0, -150, 100)

    s.hold()


if __name__ == "__main__":
    main()