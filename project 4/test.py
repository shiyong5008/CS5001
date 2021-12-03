# NEU CS5001 Project 4 graphicsPlus drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import graphicsPlus as gr

def main(argv):
    win=gr.GraphWin("My window",500,500)
    c=gr.Circle(gr.Point(250, 250),10)
    c.draw(win)
    win.getMouse()
    c.setFill("green")
    win.getMouse()
    c.move(50,-40)
    win.getMouse()
    win.close()
    return
if __name__=="__main__":
    main([])