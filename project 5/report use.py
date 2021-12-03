# NEU CS5001 Project 4 graphicsPlus drawing
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import graphicsPlus as g
import random

def riverboat(x, y, scale): # define the river and boat
    riverlist = [g.Point(x-1600*scale, y+10*scale), # river point list
                 g.Point(x+100*scale, y+20*scale),
                 g.Point(x+200*scale, y+10*scale),
                 g.Point(x+250*scale, y+30*scale),
                 g.Point(x+300*scale, y+20*scale),
                 g.Point(x+450*scale, y+30*scale),
                 g.Point(x+500*scale, y+10*scale),
                 g.Point(x+600*scale, y+20*scale),
                 g.Point(x+750*scale, y+30*scale),
                 g.Point(x+1600*scale, y+10*scale),
                 g.Point(x + 1600 * scale, y + 110 * scale),
                 g.Point(x + 750 * scale, y + 130 * scale),
                 g.Point(x + 600 * scale, y + 120 * scale),
                 g.Point(x + 500 * scale, y + 110 * scale),
                 g.Point(x + 450 * scale, y + 130 * scale),
                 g.Point(x + 300 * scale, y + 120 * scale),
                 g.Point(x + 250 * scale, y + 130 * scale),
                 g.Point(x + 200 * scale, y + 110 * scale),
                 g.Point(x + 100 * scale, y + 120 * scale),
                 g.Point(x - 1600 * scale, y + 110 * scale)]
    riverflow=g.Polygon(riverlist) #river drawing
    riverflow.setFill("blue")
    riverflow.setOutline("green")
    riverflow.setWidth(5)

    boatlist1 = [g.Point(x-300*scale, y+70*scale), # boat1 point list
                 g.Point(x-250*scale, y+60*scale),
                 g.Point(x-200*scale, y+60*scale),
                 g.Point(x-200*scale, y+80*scale),
                 g.Point(x-250*scale, y+80*scale)]
    boatbody1=g.Polygon(boatlist1) # boat1 drawing
    boatbody1.setFill("red")
    boatbody1.setOutline("black")
    boatbody1.setWidth(5)
    boatlist2 = [g.Point(x-100*scale, y+70*scale), # boat2 point list
                 g.Point(x-50*scale, y+60*scale),
                 g.Point(x+0*scale, y+60*scale),
                 g.Point(x+0*scale, y+80*scale),
                 g.Point(x-50*scale, y+80*scale)]
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

# this is the birds list function
def init_birds(x,y,scale):
    bird1list = [g.Point(x+10*scale, y+10*scale), # bird1 point list
                 g.Point(x+20*scale, y+10*scale),
                 g.Point(x+20*scale, y+15*scale),
                 g.Point(x+30*scale, y+15*scale),
                 g.Point(x+40*scale, y+5*scale),
                 g.Point(x+40*scale, y+15*scale),
                 g.Point(x+60*scale, y+15*scale),
                 g.Point(x+60*scale, y+20*scale),
                 g.Point(x+40*scale, y+20*scale),
                 g.Point(x+40*scale, y+30*scale),
                 g.Point(x + 30 * scale, y + 20 * scale),
                 g.Point(x + 20 * scale, y + 20 * scale),
                 g.Point(x + 20 * scale, y + 25 * scale),
                 g.Point(x + 10 * scale, y + 25 * scale),
                 g.Point(x + 0 * scale, y + 17.5 * scale)]
    bird1=g.Polygon(bird1list) #bird1 drawing
    bird1.setFill("blue")
    bird1.setOutline("red")
    bird1.setWidth(1)

    bird2list = [g.Point(x+60*scale, y+30*scale), # bird2 point list
                 g.Point(x+70*scale, y+30*scale),
                 g.Point(x+70*scale, y+35*scale),
                 g.Point(x+80*scale, y+35*scale),
                 g.Point(x+90*scale, y+25*scale),
                 g.Point(x+90*scale, y+35*scale),
                 g.Point(x+110*scale, y+35*scale),
                 g.Point(x+110*scale, y+40*scale),
                 g.Point(x+90*scale, y+40*scale),
                 g.Point(x+90*scale, y+50*scale),
                 g.Point(x + 80 * scale, y + 40 * scale),
                 g.Point(x + 70 * scale, y + 40 * scale),
                 g.Point(x + 70 * scale, y + 45 * scale),
                 g.Point(x + 60 * scale, y + 45 * scale),
                 g.Point(x + 50 * scale, y + 37.5 * scale)]
    bird2=g.Polygon(bird2list) #bird2 drawing
    bird2.setFill("pink")
    bird2.setOutline("red")
    bird2.setWidth(1)

    bird3list = [g.Point(x-10*scale, y+10*scale), # bird3 point list
                 g.Point(x-20*scale, y+10*scale),
                 g.Point(x-20*scale, y+15*scale),
                 g.Point(x-30*scale, y+15*scale),
                 g.Point(x-40*scale, y+5*scale),
                 g.Point(x-40*scale, y+15*scale),
                 g.Point(x-60*scale, y+15*scale),
                 g.Point(x-60*scale, y+20*scale),
                 g.Point(x-40*scale, y+20*scale),
                 g.Point(x-40*scale, y+30*scale),
                 g.Point(x - 30 * scale, y + 20 * scale),
                 g.Point(x - 20 * scale, y + 20 * scale),
                 g.Point(x - 20 * scale, y + 25 * scale),
                 g.Point(x - 10 * scale, y + 25 * scale),
                 g.Point(x + 0 * scale, y + 17.5 * scale)]
    bird3=g.Polygon(bird3list) #bird3 drawing
    bird3.setFill("blue")
    bird3.setOutline("red")
    bird3.setWidth(1)

    bird4list = [g.Point(x+40*scale, y+30*scale), # bird4 point list
                 g.Point(x+30*scale, y+30*scale),
                 g.Point(x+30*scale, y+35*scale),
                 g.Point(x+20*scale, y+35*scale),
                 g.Point(x+10*scale, y+25*scale),
                 g.Point(x+10*scale, y+35*scale),
                 g.Point(x-10*scale, y+35*scale),
                 g.Point(x-10*scale, y+40*scale),
                 g.Point(x+10*scale, y+40*scale),
                 g.Point(x+10*scale, y+50*scale),
                 g.Point(x + 20 * scale, y + 40 * scale),
                 g.Point(x + 30 * scale, y + 40 * scale),
                 g.Point(x + 30 * scale, y + 45 * scale),
                 g.Point(x + 40 * scale, y + 45 * scale),
                 g.Point(x + 50 * scale, y + 37.5 * scale)]
    bird4=g.Polygon(bird4list) #bird4 drawing
    bird4.setFill("pink")
    bird4.setOutline("red")
    bird4.setWidth(1)

    test4=[bird1,bird2,bird3,bird4]
    return test4

#this is the birds animation fly to left and right
def animate_birds(test4,frame,win):
    bird1=test4[0]
    bird2=test4[1]
    bird3=test4[2]
    bird4=test4[3]

    if frame % 1000 < 500: # when frame range to fly to right
        bird2.setFill("whitesmoke")
        bird2.setOutline("whitesmoke")
        bird4.setFill("pink")
        bird4.setOutline("red")
        bird1.setFill("whitesmoke")
        bird1.setOutline("whitesmoke")
        bird3.setFill("blue")
        bird3.setOutline("red")
        for item in test4:
            item.move(2, 0)
    else: # when frame range to fly to left
        bird4.setFill("whitesmoke")
        bird4.setOutline("whitesmoke")
        bird2.setFill("pink")
        bird2.setOutline("red")
        bird3.setFill("whitesmoke")
        bird3.setOutline("whitesmoke")
        bird1.setFill("blue")
        bird1.setOutline("red")
        for item in test4:
            item.move(-2, 0)

def animate_riverboat(test,frame,win):
    if frame % 500 == 0:
        for item in test:
            item.move(win.getWidth(), 0)
    else:
        for item in test:
            item.move(-2, 0)

def animate_village(test2,frame,win):
    village1=test2[0]
    village2=test2[1]
    village3=test2[2]
    village4=test2[3]
    village5=test2[4]
    village6=test2[5]
    village7=test2[6]
    village8=test2[7]

    if frame % 100 < 50: # when frame range to change color
        village1.setFill("orange")
        village2.setFill("yellow")
        village3.setFill("green")
        village4.setFill("red")
        village5.setFill("light blue")
        village6.setFill("yellow")
        village7.setFill("grey")
        village8.setFill("pink")

        for item in test2:
            item.move(0.2, 0)
    else: # when frame range to change color
        village1.setFill("green")
        village2.setFill("red")
        village3.setFill("blue")
        village4.setFill("pink")
        village5.setFill("grey")
        village6.setFill("black")
        village7.setFill("purple")
        village8.setFill("brown")
        for item in test2:
            item.move(-0.2, 0)

# testing codes
def main():
    win=g.GraphWin("My window", 1000, 600)
    test=riverboat(100, 300, 1)
    for thing in test:
        thing.draw(win)

    test2=village(500, 300, 1)
    for thing in test2:
        thing.draw(win)

    test2=village(100, 300, 1)
    for thing in test2:
        thing.draw(win)

    test4 = init_birds(-50,0,2)
    for thing in test4:
        thing.draw(win)

    for i in range(30):
        test3=grass(100, 300, 1)
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
        animate_birds( test4, frame, win )
        # call the boats and river animation fly to right and left
        animate_riverboat(test, frame, win)
        # call the village animation fly to right and left
        animate_village(test2, frame, win)

        win.update()
        frame += 1

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()