# NEU CS5001 Project 5 graphicsPlus drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import graphicsPlus as g
import random
import time
import sys
import complex_shapes as com


def main():
    k = int(sys.argv[1])  # scale control at terminal input

    win=g.GraphWin("My window", 1000, 600)
    test=com.riverboat(100, 300, k)
    for thing in test:
        thing.draw(win)

    test2=com.village(500, 300, k)
    for thing in test2:
        thing.draw(win)

    test2=com.village(100, 300, k)
    for thing in test2:
        thing.draw(win)

    test4 = com.init_birds(-50,0,2)
    for thing in test4:
        thing.draw(win)

    for i in range(30):
        test3=com.grass(100, 300, 1)
        for thing in test3:
          thing.draw(win)

    frame = 0
    while True:
        key = win.checkKey()
        if key == 'q':
            break
        if win.checkMouse() != None:
            break

        # call the birds animation fly to right and left
        com.animate_birds( test4, frame, win )
        # call the boats and river animation fly to right and left
        com.animate_riverboat(test, frame, win)
        # call the village animation fly to right and left
        com.animate_village(test2, frame, win)

        win.update()
        frame += 1

    win.getMouse()
    win.close()

if __name__=="__main__":
    main()

# due to I am in China that can not access Google Drive, or other Google products,
# so got noted with professor that I sent the video thru email to professor already, thanks!