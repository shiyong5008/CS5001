# Bruce Maxwell
# CS 5001 Spring 2021
#
# Zelle Graphics first example
#

import graphicsPlus as gr
import random

def main( argv ):

    # create a window
    win = gr.GraphWin( "My window", 500, 500 )

    # create a circle
    c = gr.Circle( gr.Point( 250, 250 ), 10 )

    # draw the circle into the window
    c.move( 50, -40 ) # relative move to a new location
    c.draw( win ) # draw into the window
    win.getMouse() # pause
    c.setFill( "green" ) # make the circle green
    win.getMouse() # pause
    c.undraw() # undraw the circle
    
    # pause until the user clicks the mouse
    win.getMouse()
    win.close() # close window

    return

def interactive():

    win = gr.GraphWin( 'interactive demo', 500, 500, False )
    r = gr.Rectangle( gr.Point( 220, 260 ), gr.Point( 280, 240 ) )
    r.setOutline( 'purple' )
    r.setFill( 'pink' )
    r.setWidth( 3 )
    r.draw( win )

    counter = 0
    falling = None

    # begin event loop
    while True: # infinite loop

        if counter % 100 == 0:
            if falling != None:
                falling.undraw()
            falling = gr.Circle( gr.Point( random.randint(0, 500), 0 ), 10 )
            falling.setFill( 'blue' )
            falling.draw(win)

        if falling != None:
            falling.move( random.randint(-3, 3), 5 )

        counter += 1

        key = win.checkKey()
        if key == 'q':
            break
        elif key == 'a': # move left
            r.move( -20, 0 )
        elif key == 'w': # move up
            r.move( 0, -20 )
        elif key == 's': # move down
            r.move( 0, 20 )
        elif key == 'd': # move right
            r.move( 20, 0 )

        win.update() # manually update the window

    print("Terminating")
    win.close()


if __name__ == "__main__":
    #main( [] )
    interactive()
