# NEU CS5001 week8 project 10 turtle_interpreter.py version 4
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle as t
import random
import sys

class TurtleInterpreter:

    initialized = False

    def __init__(self, dx=800, dy=800):
        if TurtleInterpreter.initialized:
            return
        TurtleInterpreter.initialized = True

    # call turtle.setup with dx and dy as the arguments
        t.setup(width=dx, height=dy)
    # set the turtle tracer to false (optional)
        t.tracer(False)

        # add two fields to the object called style and jitterSigma
        self.style="normal"
        self.jitterSigma=5
    def setStyle(self, s):
        self.style=s
    def setJitter(self, j):
        self.jitterSigma=j
    def getStyle(self):
        return self.style
    def getJitter(self):
        return self.jitterSigma

    def forward(self, distance):
        # if self.style is equal to 'jitter'
        if self.style=="jitter":
            # assign to x0 and y0 the result of turtle.position()
            x0,y0=t.position()
            # pick up the turtle
            t.up()
            # have the turtle go forward by distance
            t.forward(distance)
            # assign to xf and yf the result of turtle.position()
            xf,yf=t.position()
            # assign to curwidth the result of turtle.width()
            curwidth=t.width()

            # assign to jx the result of random.gauss(0, self.jitterSigma)
            jx=random.gauss(0, self.jitterSigma)
            # assign to jy the result of random.gauss(0, self.jitterSigma)
            jy = random.gauss(0, self.jitterSigma)
            # assign to kx the result of random.gauss(0, self.jitterSigma)
            kx = random.gauss(0, self.jitterSigma)
            # assign to ky the result of random.gauss(0, self.jitterSigma)
            ky = random.gauss(0, self.jitterSigma)

            # set the turtle width to (curwidth + random.randint(0, 2))
            t.width(curwidth + random.randint(0, 2))
            # have the turtle go to (x0 + jx, y0 + jy)
            t.goto(x0 + jx, y0 + jy)
            # put the turtle down
            t.down()
            # have the turtle go to (xf + kx, yf + ky)
            t.goto(xf + kx, yf + ky)
            # pick up the turtle
            t.up()
            # have the turtle go to (xf, yf)
            t.goto(xf, yf)
            # set the turtle width to curwidth
            t.width(curwidth)
            # put the turtle down
            t.down()

        # elif self.style is equal to 'jitter3'
        elif self.style == "jitter3":
            # Part 1: Figure out and store the true start point, true end point.
            # assign to x0 and y0 the result of turtle.position()
            x0, y0 = t.position()
            # pick up the turtle
            t.up()
            # have the turtle go forward by distance
            t.forward(distance)
            # assign to xf and yf the result of turtle.position()
            xf, yf = t.position()
            # assign to curwidth the result of turtle.width()
            curwidth = t.width()

            # Part 2: Draw the alternative visual representation.
            for i in range(3):
                # assign to jx the result of random.gauss(0, self.jitterSigma)
                jx = random.gauss(0, self.jitterSigma)
                # assign to jy the result of random.gauss(0, self.jitterSigma)
                jy = random.gauss(0, self.jitterSigma)
                # assign to kx the result of random.gauss(0, self.jitterSigma)
                kx = random.gauss(0, self.jitterSigma)
                # assign to ky the result of random.gauss(0, self.jitterSigma)
                ky = random.gauss(0, self.jitterSigma)

                # set the turtle width to (curwidth + random.randint(0, 2))
                t.width(curwidth + random.randint(0, 2))
                # have the turtle go to (x0 + jx, y0 + jy)
                t.goto(x0 + jx, y0 + jy)
                # put the turtle down
                t.down()
                # have the turtle go to (xf + kx, yf + ky)
                t.goto(xf + kx, yf + ky)
                # pull up and back to original at next cycle
                t.up()

            # Part 3: Pick up the pen and go to the true end point, resetting the width, etc.
            # pick up the turtle
            t.up()
            # have the turtle go to (xf, yf)
            t.goto(xf, yf)
            # set the turtle width to curwidth
            t.width(curwidth)
            # put the turtle down
            t.down()

        #Create a 'dotted' style that draws a series of circles separated by spaces.
        elif self.style == "dotted":
            radius=5
            spacing=1.5*radius

            #step1
            xi, yi = t.position()
            t.up()
            t.forward(distance)
            xf, yf = t.position()
            h=t.heading()
            c=t.color()

            #step2
            dx=xf-xi
            dy=yf-yi
            steps=distance/spacing
            stepsize=spacing/distance

            for i in range(int(steps)):
                jx = random.gauss(0, self.jitterSigma)
                jy = random.gauss(0, self.jitterSigma)
                rad = random.gauss(radius, self.jitterSigma)
                rad=max(rad,2)

                xt=xi+dx*stepsize*i+jx
                yt=yi+dy*stepsize*i+jy
                t.goto(xt,yt)
                t.color(random.random(),random.random(),random.random())
                t.down()
                t.begin_fill()
                t.circle(rad)
                t.end_fill()
                t.up()

            #step3
            t.color(c[0])
            t.goto(xf,yf)
            t.setheading(h)
            t.down()






        # else
        else:
            # have the turtle go foward by distance
            t.forward(distance)

    def drawString(self, dstring, distance, angle):
        """ Interpret the characters in string dstring as a series
        of turtle commands. Distance specifies the distance
        to travel for each forward command. Angle specifies the
        angle (in degrees) for each right or left command. The list of
        turtle supported turtle commands is:
        F : forward
        - : turn right
        + : turn left
        [ : save the turtle's heading and position
        ] : restore the turtle's heading and position
        """

        # assign to modval the value None
        modval=None
        # assign to modgrab the value False
        modgrab=False

        # assign to stack the empty list
        stack=[]
        colorstack = []


        # for each character c in dstring
        # for c in dstring:
        for c in dstring:
            # if c is equal to '('
            if c=='(':
                # assign to modval the empty string
                modval=""
                # assign to modgrab the value True
                modgrab=True
                # continue
                continue
            # else if c is equal to ')'
            elif c==')':
                # assign to modval the result of casting modval to a float
                modval=float(modval)
                # assign to modgrab False
                modgrab=False
                # continue
                continue
                # else if modgrab (is True)
            elif modgrab:
                # add to modval the character c
                modval+=c
                # continue
                continue

            # if c is equal to 'F'
            elif c=='F':
                # tell the turtle go forward by distance
                # self.forward(distance)

                # if modval is equal to None
                if modval==None:
                    # call self.forward with the argument distance
                    self.forward(distance)
                # else
                else:
                    # call self.forward with the argument distance * modval
                    self.forward(distance*modval)
            elif c=='f':
                # tell the turtle go forward by distance
                # self.forward(distance)

                # if modval is equal to None
                if modval==None:
                    # call self.forward with the argument distance
                    self.forward(distance)
                # else
                else:
                    # call self.forward with the argument distance * modval
                    self.forward(distance*modval)

            # if c is '!'
            elif c=='!':
                # if modval is equal to None
                if modval==None:
                    # assign to w the result of calling turtle.width()
                    w=t.width()
                    # if w is greater than 1
                    if w>1:
                        # call turtle.width with w-1 as the argument
                        t.width(w-1)
                # else
                else:
                    # call turtle.width with modval as the argument
                    t.width(modval)

            # else if c is equal to '-'
            elif c=='-':
                # tell the turtle to turn right by angle
                # t.right(angle)
                if modval==None:
                    t.right(angle)
                else:
                    t.right(modval)
            # else if c is equal to '+'
            elif c=='+':
                # tell the turtle to turn left by angle
                # t.left(angle)
                if modval==None:
                    t.left(angle)
                else:
                    t.left(modval)

            # else if c is equal to '['
            elif c=='[':
                  # append to stack the position of the turtle (position method)
                stack.append(t.position())
                  # append to stack the heading of the turtle (heading method)
                stack.append(t.heading())
            # else if c is equal to ']'
            elif c==']':
                  # tell the turtle to pick up pen
                t.up()
                  # call the setheading method of the turtle and pass it the value popped off stack
                t.setheading(stack.pop())
                  # call the goto method of the turtle and pass it the value popped off stack
                t.goto(stack.pop())
                  # tell the turtle to put down pen
                t.down()
            # Define < to push a color on the color stack
            elif c=='<':
                colorstack.append(t.color()[0])
            # Define > to pop a color off the color stack
            elif c=='>':
                t.color(colorstack.pop())
            # Define g as green, y as yellow, r as red
            elif c=='g':
                t.color(0.15, 0.5, 0.2)
            elif c=='y':
                t.color(0.8, 0.8, 0.3)
            elif c=='r':
                t.color(0.7, 0.2, 0.3)
            elif c=='L':
                t.begin_fill()
                for i in range(3):
                    t.forward(5)
                    t.left(120)
                t.end_fill()
            elif c=='{':
                t.begin_fill()
            elif c=='}':
                t.end_fill()

            modval=None

        # call turtle.update() (not in the for loop)
        t.update()

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' key'''

        # Hide the turtle cursor and update the screen
        t.hideturtle()
        t.update()

        # Close the window when users presses the 'q' key
        t.onkey(t.bye, 'q')

        # Listen for the q button press event
        t.listen()

        # Have the turtle listen for a click
        t.exitonclick()


    # Add the following methods to your turtle interpreter class.
    def place(self, xpos, ypos, angle=None):
        t.up()
        t.goto(xpos, ypos)
        if angle!=None:
            self.orient(angle)
        t.down()

    def orient(self, angle):
        t.setheading(angle)

    def goto(self, xpos, ypos):
        t.up()
        t.goto(xpos, ypos)
        t.down()

    def setColor(self, c):
        t.color(c)

    def setWidth(self, w):
        t.width(w)
