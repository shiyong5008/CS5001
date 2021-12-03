# NEU CS5001 week8 project 9 turtle_interpreter.py version 3
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

        # assign to stack the empty list
        stack=[]
        colorstack = []

        # for each character c in dstring
        for c in dstring:
            # if c is equal to 'F'
            if c=='F':
                  # tell the turtle go forward by distance
                t.forward(distance)
            # else if c is equal to '-'
            elif c=='-':
                  # tell the turtle to turn right by angle
                t.right(angle)
            # else if c is equal to '+'
            elif c=='+':
                  # tell the turtle to turn left by angle
                t.left(angle)
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
