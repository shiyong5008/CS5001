# Bruce Maxwell
# CS 5001 Spring 2021
#
# Complex object example
#
import graphicsPlus as gr
import random

# creates and returns a list of objects
# should be a beautiful whale with a city on top
def citywhale( x, y, scale ):

    # define a polygon for the body, list of points
    bodylist = [ gr.Point( x + 5*scale, y - 5*scale ), # starts at lower left of the whale body
                 gr.Point( x + 25*scale, y - 2*scale ),
                 gr.Point( x + 45*scale, y - 8*scale ),
                 gr.Point( x + 70*scale, y - 15*scale ),
                 gr.Point( x + 100*scale, y - 6*scale ),
                 gr.Point( x + 90*scale, y - 20*scale ),
                 gr.Point( x + 100*scale, y - 34*scale ),
                 gr.Point( x + 80*scale, y - 25*scale ),
                 gr.Point( x + 55*scale, y - 27*scale ),
                 gr.Point( x + 45*scale, y - 30*scale ),
                 gr.Point( x + 30*scale, y - 30*scale ),
                 gr.Point( x + 24*scale, y - 27*scale ),
                 gr.Point( x + 8*scale, y - 24*scale ),
                 gr.Point( x - 8*scale, y - 25*scale ) ]
    whalebody = gr.Polygon( bodylist )
    whalebody.setFill( "purple" )
    whalebody.setOutline( "dark blue" )
    whalebody.setWidth( 4 )

    # define a polygon for the mouth
    mouthlist = [ gr.Point( x + 24*scale, y - 27*scale ),
                 gr.Point( x + 8*scale, y - 24*scale ),
                 gr.Point( x - 8*scale, y - 25*scale ),
                 gr.Point( x + 8*scale, y - 30*scale ) ]
    whalemouth = gr.Polygon( mouthlist )
    whalemouth.setFill( "grey" )
    whalemouth.setOutline( "dark blue" )
    whalemouth.setWidth( 2 )

    c1 = gr.Circle( gr.Point( x + 20*scale, y - 20*scale ), 5 )
    c1.setFill( "black" )
    
    # define four rectangles for the city
    b1 = gr.Rectangle( gr.Point( x+30*scale, y-30*scale ),
                       gr.Point( x+34*scale, y-44*scale ) )
    b1.setFill( 'turquoise' )

    b2 = gr.Rectangle( gr.Point( x+34*scale, y-30*scale ),
                       gr.Point( x+38*scale, y-50*scale ) )
    b2.setFill( 'red' )

    b3 = gr.Rectangle( gr.Point( x+38*scale, y-30*scale ),
                       gr.Point( x+42*scale, y-40*scale ) )
    b3.setFill( 'green' )

    b4 = gr.Rectangle( gr.Point( x+42*scale, y-30*scale ),
                       gr.Point( x+46*scale, y-38*scale ) )
    b4.setFill( 'orange' )
                       
    # put all of these objects into a list
    whale = [ whalebody, whalemouth, c1, b1, b2, b3, b4 ]

    # return the list
    return whale

# draws the graphics objects in listofStuff into win
def draw( listofStuff, win ):
    for item in listofStuff:
        item.draw(win)

# calls the move method for each graphics object in listofStuff
# moves the object by dx and dy
def move( listofStuff, dx, dy ):
    for item in listofStuff:
        item.move( dx, dy )

def main():

    # create a window and tell it not to auto-update
    win = gr.GraphWin( 'whales', 1000, 1000, False )

    # whale is a list of graphics objects
    whale = citywhale( 500, 500, 2.0 )

    whale2 = citywhale( 200, 800, 4.0 )

    # draw each graphics object into the window
    #for thing in whale:
    #    thing.draw( win )
    draw( whale, win )
    draw( whale2, win )

    while True:

        # check for a keystroke
        key = win.checkKey()
        if key == 'q':
            break # exit the loop

        # move the whales left
        move( whale, -1, 0 )
        move( whale2, -2, 0 )

        # using the whale's eye to check it's horizontal location
        p1 = whale[2].getCenter()
        # if the eye goes out of bounds, move it right
        if p1.x < 0:
            move( whale, win.getWidth(), 0 )
            # change the color when it shifts
            whale[0].setFill( gr.color_rgb( random.randint(0, 255),
                                            random.randint(0, 255),
                                            random.randint(0, 255) ) )

        # same check for whale 2
        p2 = whale2[2].getCenter()
        if p2.x < 0:
            move( whale2, win.getWidth(), 0 )
            whale2[0].setFill( gr.color_rgb( random.randint(0, 255),
                                            random.randint(0, 255),
                                            random.randint(0, 255) ) )

        # need to update each time for smooth motion
        win.update()

    # wait for a mouse click
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
