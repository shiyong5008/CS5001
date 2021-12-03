# NEU CS5001 Project 4 graphicsPlus drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import graphicsPlus as g
import complex_shapes as co
import sys



def main():
    scale = float(sys.argv[1])  # scale control at terminal command line input
    win=g.GraphWin("My window", 1000, 600) # open window

    test=co.riverboat(100, 200, scale) # call the riverboat function
    for thing in test:
        thing.draw(win)

    test2=co.village(500, 200, scale) # call the village function
    for thing in test2:
        thing.draw(win)

    test2=co.village(100, 200, scale) # call the village function in a different location
    for thing in test2:
        thing.draw(win)

    for i in range(30): # use for loop to draw more random grass
        test3=co.grass(100, 200, scale) # call the grass function
        for thing in test3:
            thing.draw(win)

    win.getMouse() # wait for mouse click
    win.close() # close window

if __name__ == "__main__": # high level code to prevent execution as need
    main()