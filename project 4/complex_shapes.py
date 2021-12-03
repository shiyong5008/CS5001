# NEU CS5001 Project 4 graphicsPlus drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import graphicsPlus as g
import random

def riverboat(x, y, scale): # define the river and boat
    riverlist = [g.Point(x+10*scale, y+10*scale), # river point list
                 g.Point(x+100*scale, y+20*scale),
                 g.Point(x+200*scale, y+10*scale),
                 g.Point(x+250*scale, y+30*scale),
                 g.Point(x+300*scale, y+20*scale),
                 g.Point(x+450*scale, y+30*scale),
                 g.Point(x+500*scale, y+10*scale),
                 g.Point(x+600*scale, y+20*scale),
                 g.Point(x+750*scale, y+30*scale),
                 g.Point(x+800*scale, y+10*scale),
                 g.Point(x + 800 * scale, y + 110 * scale),
                 g.Point(x + 750 * scale, y + 130 * scale),
                 g.Point(x + 600 * scale, y + 120 * scale),
                 g.Point(x + 500 * scale, y + 110 * scale),
                 g.Point(x + 450 * scale, y + 130 * scale),
                 g.Point(x + 300 * scale, y + 120 * scale),
                 g.Point(x + 250 * scale, y + 130 * scale),
                 g.Point(x + 200 * scale, y + 110 * scale),
                 g.Point(x + 100 * scale, y + 120 * scale),
                 g.Point(x + 10 * scale, y + 110 * scale)]
    riverflow=g.Polygon(riverlist) #river drawing
    riverflow.setFill("blue")
    riverflow.setOutline("green")
    riverflow.setWidth(5)

    boatlist1 = [g.Point(x+200*scale, y+70*scale), # boat1 point list
                 g.Point(x+250*scale, y+60*scale),
                 g.Point(x+300*scale, y+60*scale),
                 g.Point(x+300*scale, y+80*scale),
                 g.Point(x+250*scale, y+80*scale)]
    boatbody1=g.Polygon(boatlist1) # boat1 drawing
    boatbody1.setFill("red")
    boatbody1.setOutline("black")
    boatbody1.setWidth(5)
    boatlist2 = [g.Point(x+500*scale, y+70*scale), # boat2 point list
                 g.Point(x+550*scale, y+60*scale),
                 g.Point(x+600*scale, y+60*scale),
                 g.Point(x+600*scale, y+80*scale),
                 g.Point(x+550*scale, y+80*scale)]
    boatbody2=g.Polygon(boatlist2) # boat2 drawing
    boatbody2.setFill("orange")
    boatbody2.setOutline("black")
    boatbody2.setWidth(5)

    test=[riverflow,boatbody1,boatbody2]

    return test

def village(x, y, scale): # define the village
    b1=g.Rectangle(g.Point(x+100*scale, y-10*scale), # house box point list
                    g.Point(x+150*scale, y-50*scale))
    b1.setFill("orange")
    c1=g.Circle(g.Point(x+125*scale, y-60*scale),30*scale) # house roof box point list
    c1.setFill("pink")

    b2=g.Rectangle(g.Point(x+300*scale, y-10*scale), # house box point list
                    g.Point(x+350*scale, y-50*scale))
    b2.setFill("grey")
    c2=g.Circle(g.Point(x+325*scale, y-60*scale),30*scale) # house roof box point list
    c2.setFill("yellow")

    b3=g.Rectangle(g.Point(x+200*scale, y-10*scale), # tree box point list
                    g.Point(x+220*scale, y-150*scale))
    b3.setFill("brown")
    c3=g.Circle(g.Point(x+210*scale, y-150*scale),50*scale) # tree roof box point list
    c3.setFill("green")

    b4=g.Rectangle(g.Point(x+250*scale, y-10*scale), # tree box point list
                    g.Point(x+270*scale, y-130*scale))
    b4.setFill("black")
    c4=g.Circle(g.Point(x+260*scale, y-130*scale),50*scale) # tree roof box point list
    c4.setFill("light green")

    test2 = [b1, b2, c1, c2, b3, c3, b4, c4]

    return test2

def grass(x,y, scale): # define the grass
    cc1 = g.Circle(g.Point(x + 250 * (random.uniform(0.2, 3)) * scale, y + 150 * (random.uniform(1, 1.5)) * scale),
                   random.uniform(5, 10)) # random grass generate
    cc1.setFill("green")
    cc2 = g.Circle(g.Point(x + 250 * (random.uniform(0.2, 3)) * scale, y + 150 * (random.uniform(1, 1.5)) * scale),
                   random.uniform(5, 10)) # random grass generate
    cc2.setFill("green")
    test3=[cc1, cc2]

    return test3

# testing codes
def main():
   win=g.GraphWin("My window", 1000, 600)
   test=riverboat(100, 200, 1)
   for thing in test:
       thing.draw(win)

   test2=village(500, 200, 1)
   for thing in test2:
       thing.draw(win)

   test2=village(100, 200, 1)
   for thing in test2:
       thing.draw(win)

   for i in range(30):
       test3=grass(100, 200, 1)
       for thing in test3:
           thing.draw(win)

   win.getMouse()
   win.close()

if __name__ == "__main__":
   main()