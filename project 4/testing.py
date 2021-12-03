# NEU CS5001 Project 4 graphicsPlus drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import graphicsPlus as g
import complex_shapes as co

def main():
    win=g.GraphWin("My window", 1000, 600) # open window
    for k in range(1,4):
        # test=co.riverboat(100*i*0.3, 200*i*0.3, 1*i*0.3) # call the riverboat function
        # for thing in test:
        #     thing.draw(win)

        # test2=co.village(500*i*0.3, 200*i*0.3, 1*i*0.3) # call the village function
        # for thing in test2:
        #     thing.draw(win)
    #
        # test2=co.village(100, 200, 1) # call the village function in a different location
        # for thing in test2:
        #     thing.draw(win)
    #
        for i in range(30): # use for loop to draw more random grass
            test3=co.grass(100*k*0.3, 200*k*0.3, 1*k*0.3) # call the grass function
            for thing in test3:
                thing.draw(win)

    win.getMouse() # wait for mouse click
    win.close() # close window

if __name__ == "__main__": # high level code to prevent execution as need
    main()