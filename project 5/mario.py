# Bruce Maxwell
# CS 5001 Spring 2021
# Creating Mario
#

import graphicsPlus as gr
import time

def red_shirt_points( x, y, scale, armdown ):

    if armdown:
        points = [ gr.Point( x + 0*scale, y - 120*scale ),
                gr.Point( x + 0*scale, y - 150*scale ),
                gr.Point( x - 10*scale, y - 150 *scale ),
                gr.Point( x - 10*scale, y - 100*scale ),
                gr.Point( x - 30*scale, y - 100*scale ),
                gr.Point( x - 30*scale, y - 170*scale ),
                gr.Point( x + 90*scale, y - 170*scale ),
                gr.Point( x + 90*scale, y - 100*scale ),
                gr.Point( x + 70*scale, y - 100*scale ),
                gr.Point( x + 70*scale, y - 150*scale ),
                gr.Point( x + 60*scale, y - 150*scale ),
                gr.Point( x + 60*scale, y - 120*scale ) ]
    else:
        points = [ gr.Point( x + 0*scale, y - 120*scale ),
                gr.Point( x + 0*scale, y - 150*scale ),
                gr.Point( x - 10*scale, y - 150 *scale ),
                gr.Point( x - 10*scale, y - 100*scale ),
                gr.Point( x - 30*scale, y - 100*scale ),
                gr.Point( x - 30*scale, y - 170*scale ),
                gr.Point( x + 70*scale, y - 170*scale ), # right arm
                gr.Point( x + 70*scale, y - 220*scale ),
                gr.Point( x + 90*scale, y - 220*scale ),
                gr.Point( x + 90*scale, y - 150*scale ),
                gr.Point( x + 60*scale, y - 150*scale ),
                gr.Point( x + 60*scale, y - 120*scale ) ]

    return points

def init_mario( x, y, scale ):

    # Overalls as a polygon
    points = [ gr.Point( x + 0*scale, y - 0*scale ),
               gr.Point( x + 0*scale, y - 120*scale ),
               gr.Point( x + 10*scale, y - 120*scale ),
               gr.Point( x + 10*scale, y - 170*scale ),
               gr.Point( x + 20*scale, y - 170*scale ),
               gr.Point( x + 20*scale, y - 120*scale ),
               gr.Point( x + 40*scale, y - 120*scale ),
               gr.Point( x + 40*scale, y - 170*scale ),
               gr.Point( x + 50*scale, y - 170*scale ),
               gr.Point( x + 50*scale, y - 120*scale ),
               gr.Point( x + 60*scale, y - 120*scale ),
               gr.Point( x + 60*scale, y - 0*scale ),
               gr.Point( x + 40*scale, y - 0*scale ),
               gr.Point( x + 40*scale, y - 60*scale ),
               gr.Point( x + 20*scale, y - 60*scale ),
               gr.Point( x + 20*scale, y - 0*scale ) ]
    overalls = gr.Polygon( points )
    overalls.setFill( 'steel blue' )

    # red shirt
    shirt = gr.Polygon( red_shirt_points(x, y, scale, False ) )
    shirt.setFill( 'red' )

    head = gr.Circle( gr.Point( x + 30*scale, y - 195*scale ), 25*scale )
    head.setFill( 'salmon' )

    points = [ gr.Point( x - 15*scale, y - 210*scale ),
               gr.Point( x - 15*scale, y - 215*scale ),
               gr.Point( x + 5*scale, y - 215*scale ),
               gr.Point( x + 10*scale, y - 235*scale ),
               gr.Point( x + 50*scale, y - 235*scale ),
               gr.Point( x + 60*scale, y - 210*scale ) ]
    hat = gr.Polygon( points )
    hat.setFill( 'red' )

    points = [ gr.Point( x + 5*scale, y - 175*scale ),
               gr.Point( x + 10*scale, y - 180*scale ),
               gr.Point( x + 20*scale, y - 182*scale ),
               gr.Point( x + 40*scale, y - 182*scale ),
               gr.Point( x + 50*scale, y - 180*scale ),
               gr.Point( x + 55*scale, y - 175*scale ),
               gr.Point( x + 55*scale, y - 178*scale ),
               gr.Point( x + 50*scale, y - 183*scale ),
               gr.Point( x + 40*scale, y - 185*scale ),
               gr.Point( x + 20*scale, y - 185*scale ),
               gr.Point( x + 10*scale, y - 183*scale ),
               gr.Point( x + 5*scale, y - 178*scale )]
    moustache = gr.Polygon( points )
    moustache.setFill( 'black' )

    lefteye = gr.Circle( gr.Point( x + 22*scale, y - 200*scale ), 3 )
    righteye = gr.Circle( gr.Point( x + 38*scale, y - 200*scale ), 3 )
    lefteye.setFill( 'black' )
    righteye.setFill( 'black' )

    mario = [ shirt, overalls, head, hat, moustache, lefteye, righteye ]

    return mario

# pass in frame number, object list, window
def animate_mario( mario, frame, win ): 
    moustache = mario[4]

    if frame % 20 == 0:
        # move moustache up
        moustache.move( 0, -5 )

    elif frame % 20 == 10:
        # move moustache down
        moustache.move( 0, 5 )

    if frame % 80 == 0: # starting move right
        mario[0].undraw()
        # get the x, y values from overalls
        pts = mario[1].getPoints() # first point is the anchor
        # scale factor is difference in y values of first two points / 120
        scale = (pts[0].getY() - pts[1].getY()) / 120
        newshirt = gr.Polygon( red_shirt_points( pts[0].getX(), pts[0].getY(), scale, False ) )
        newshirt.setFill( 'red' )
        newshirt.draw(win)
        mario[1].undraw()
        mario[1].draw(win) # overdrawing the shirt
        mario[0] = newshirt

    elif frame % 80 == 40: # starting move left
        mario[0].undraw()
        # get the x, y values from overalls
        pts = mario[1].getPoints() # first point is the anchor
        # scale factor is difference in y values of first two points / 120
        scale = (pts[0].getY() - pts[1].getY()) / 120
        newshirt = gr.Polygon( red_shirt_points( pts[0].getX(), pts[0].getY(), scale, True ) )
        newshirt.setFill( 'red' )
        newshirt.draw(win)
        mario[1].undraw()
        mario[1].draw(win) # overdrawing the shirt
        mario[0] = newshirt

    # have all of mario move left to right
    if frame % 80 < 40: # move right with arm up
        for item in mario:
            item.move( 2, 0 )
    else:  # move left with arm down
        for item in mario:
            item.move( -2, 0)

# main function
def main( ):

    win = gr.GraphWin( 'Mario', 1000, 1000, False )

    mario = init_mario( 400, 600, 2 )

    for item in mario:
        item.draw( win )

    # time loop
    frame = 0
    while True:
        key = win.checkKey()
        if key == 'q':
            break

        if win.checkMouse() != None:
            break

        animate_mario( mario, frame, win )
        win.update()
        time.sleep( 0.033 )
        frame += 1

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()

