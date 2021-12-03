# NEU CS5001 week8 project 11 shapes.py version 4
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import turtle_interpreter

class Shape:
    def __init__(self, distance=100, angle=90, color=(0, 0, 0), istring='', style="normal", jitterSigma=0, linewidth=1):

        # create a field of self called distance and assign it distance
        self.distance=distance
        # create a field of self called angle and assign it angle
        self.angle=angle
        # create a field of self called color and assign it color
        self.color=color
        # create a field of self called string and assign it istring
        self.istring=istring

        #add fields for the style, jitterSigma, and line width
        self.style=style
        self.jitterSigma=jitterSigma
        self.linewidth=linewidth

    #getStyle, setStyle, getJitter, setJitter, getWidth, and setWidth
    def getStyle(self):
        return self.style
    def setStyle(self,style):
        self.style=style
    def getJitter(self):
        return self.jitterSigma
    def setJitter(self,jitterSigma):
        self.jitterSigma=jitterSigma
    def getWidth(self):
        return self.linewidth
    def setWidth(self,linewidth):
        self.linewidth=linewidth

    def setColor(self, c):
        self.color=c
    def setDistance(self, d):
        self.distance=d
    def setAngle(self, a):
        self.angle=a
    def setString(self, s):
        self.istring=s

    def draw(self, xpos, ypos, scale=1.0, orientation=0):
        # create a TurtleInterpreter object
        TI = turtle_interpreter.TurtleInterpreter()
        # use the TurtleInterpreter object to place the turtle at (xpos, ypos, orientation)
        TI.place(xpos, ypos, orientation)
        # use the TurtleInterpreter object to set the turtle color to self.color
        TI.setColor(self.color)

        #calls the turtle interpreter's setStyle, setJitter, and setWidth methods
        TI.setStyle(self.style)
        TI.setJitter(self.jitterSigma)
        TI.setWidth(self.linewidth)

        # use the TurtleInterpreter object draw the string
        TI.drawString(self.istring, (self.distance) * scale, self.angle)
        #    Note: use the distance, angle, and string fields of self
        #    Note: multiply the distance by the scale parameter of the method

    def hold(self):
        TI = turtle_interpreter.TurtleInterpreter()
        TI.hold()

class Square(Shape):
    def __init__(self, distance=100, color=(0, 0, 0)):
        # call the parent's __init__ method with self, distance,
        Shape.__init__(self, distance, 90, color, 'F-F-F-F-')
        #      an angle of 90, color, and the string 'F-F-F-F-'

class Triangle(Shape):
    def __init__(self, distance=100, color=(0, 0, 0)):
        # call the parent's __init__ method with self, distance,
        Shape.__init__(self, distance, 120, color, 'F-F-F-')
        #      an angle of 90, color, and the string 'F-F-F-'

class fillTriangle(Shape):
    def __init__(self, distance=100, color=(0, 0, 0)):
        # call the parent's __init__ method with self, distance,
        Shape.__init__(self, distance, 120, color, '{-F-F-F-}')
        #      an angle of 90, color, and the string '{-F-F-F}'

class fiveSide(Shape):
    def __init__(self, distance=100, color=(0, 0, 0)):
        # call the parent's __init__ method with self, distance,
        Shape.__init__(self, distance, 72, color, '{F-F-F-F-F}')
        #      an angle of 90, color, and the string '{F-F-F-F-F}'

class Side(Shape):
    def __init__(self, distance=100, color=(0, 0, 0)):
        # call the parent's __init__ method with self, distance,
        Shape.__init__(self, distance, 144, color, 'FL-FL-FL-FL-FL-')
        #      an angle of 90, color, and the string 'FL-FL-FL-FL-FL-'

class SideYellow(Shape):
    def __init__(self, distance=100, color=(0, 0, 0)):
        # call the parent's __init__ method with self, distance,
        Shape.__init__(self, distance, 144, color, 'FL-FL-FL-FL-FL-')
        #      an angle of 90, color, and the string 'FL-FL-FL-FL-FL-'


def main():

    # create a square object and draw a bunch of them
    s = Square()
    s.setColor( (0.3, 0.2, 0.9) )
    for i in range(36):
        s.draw(0, -200, scale=0.75, orientation=i*10)

    # create a triangle object and draw a bunch of them
    t = Triangle()
    t.setColor( (0.8, 0.2, 0.3) )
    for i in range(20):
        t.draw(0, 100, scale=0.8, orientation=i*18)

    # create a fillTriangle object and draw a bunch of them
    fT = fillTriangle()
    fT.setColor( (0.8, 0.2, 0.3) )
    for i in range(20):
        fT.draw(250, -100, scale=0.75, orientation=i*30)

    # create a 5sides object and draw it
    fS = fiveSide()
    fS.setColor( "red" )
    fS.draw(-300, -50, scale=0.75, orientation=0)

    # create a star object and draw a red one
    S=Side()
    S.setColor( "red" )
    S.draw(-300, 200, scale=0.75, orientation=0)

    # create a star object and draw a yellow one
    SY=SideYellow()
    SY.setColor( "yellow" )
    SY.draw(200, 200, scale=0.75, orientation=0)

    # wait
    turtle_interpreter.TurtleInterpreter().hold()


if __name__ == '__main__':
    main()