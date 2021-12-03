
import graphicsPlus as gr
import random



    # create a window
win = gr.GraphWin( "My window", 500, 500 )
r = gr.Rectangle(gr.Point(220, 260), gr.Point(280, 240))
r.setOutline('purple')
r.setFill('pink')
r.setWidth(3)
r.draw(win)

    # create a circle
while True:

    key = win.checkKey()
    if key == 'q':
        break
    elif key == 'a':  # move left
        r.move(-20, 0)
    elif key == 'w':  # move up
        r.move(0, -20)
    elif key == 's':  # move down
        r.move(0, 20)
    elif key == 'd':  # move right
        r.move(20, 0)

    # y=0
    # c = gr.Circle( gr.Point( random.randint(0, 500), y ), 10 )
    # c.setFill('green')
    # c.draw( win ) # draw into the window
    #
    # while y<400:
    #     dy=0.05
    #     c.move( 0, dy ) # relative move to a new location
    #     y+=dy
    # c.undraw() # undraw the circle


win.getMouse()
win.close() # close window

