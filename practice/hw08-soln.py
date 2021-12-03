# CS 5001 Homework 8
# Practice with classes
#

import sys

# model a ball
class Ball:

    # constructor: position, velocity, and acceleration
    # each of the values is represented by a 2-element list [x, y]
    def __init__( self, pos, vel, acc ):

        self.pos = pos[:]
        self.vel = vel[:]
        self.acc = acc[:]
        # Q1: why use the slice notation when assigning the fields?

    def getPos( self ):
        return self.pos[:]

    def setPos( self, np ):
        self.pos = np[:]

    # Q2: write get and set methods for vel and acc
    def getVel( self ):
        return self.vel[:]

    def setVel( self, nv ):
        self.vel = nv[:]

    def getAcc( self ):
        return self.acc

    def setAcc( self, na ):
        self.acc = na[:]


    # Q3: using the equation p_new = p_old + dt * vel + 0.5*dt*dt * acc
    # return the new position as a 2-element tuple (parentheses, not square brackets)
    # hint: you need to compute the x and y positions separately
    def calcPos( self, dt ):
        tx = self.pos[0] + dt * self.vel[0] + 0.5*dt*dt*self.acc[0]
        ty = self.pos[1] + dt * self.vel[1] + 0.5*dt*dt*self.acc[1]
        return (tx, ty)

    # Q4: return a list with steps 3-element tuples with (time, x, y)
    # at intervals of dt e.g. if steps is 6 and dt is 0.2, this should
    # return a list of tuples at times 0, 0.2, 0.4, 0.6, 0.8, and 1.0
    def calcTrajectory( self, dt, steps ):
        ret = []
        for i in range( steps ):
            t = dt * i
            pos = self.calcPos( dt * i )
            ret.append( ( t, pos[0], pos[1] ) )
        return ret


# test the get/set methods
def test1():

    b = Ball( [0, 1], [3, 5], [0, -10] )
    print( "position should be [0, 1]:       ", b.getPos() )
    print( "velocity should be [3, 5]:       ", b.getVel() )
    print( "acceleration should be [0, -10]: ", b.getAcc() )

# test calcPos
def test2():

    b = Ball( [0, 1], [3, 5], [0, -10] )
    print("position at time 0.0 should be [0.00, 1.00]: [%.2f, %.2f]" % b.calcPos( 0 ) )
    print("position at time 0.2 should be [0.60, 1.80]: [%.2f, %.2f]" % b.calcPos( 0.2 ) )
    print("position at time 0.5 should be [1.50, 2.25]: [%.2f, %.2f]" % b.calcPos( 0.5 ) )
    print("position at time 1.0 should be [3.00, 1.00]: [%.2f, %.2f]" % b.calcPos( 1.0 ) )

# test calcTrajectory
def test3():
    b = Ball( [0, 1], [3, 5], [0, -10] )
    data = b.calcTrajectory( 0.2, 6 )
    print("Time   X     Y")
    for entry in data:
        print("%5.2f %5.2f %5.2f" % entry )


# Q5: write a main function that takes in command line arguments for
# the time step (dt) and the total number of steps and then prints out
# the t, x, y data for a ball with the pos, vel, and acc values
# from the test3 function
def main(argv):
    if len(argv) < 3:
        print("Usage: python %s <time step> <# steps>" % argv[0])
        exit()

    try:
        dt = float(argv[1])
        steps = int(argv[2])
    except:
        print("Invalid value for dt (float) or steps (int)")
        exit()

    b = Ball( [0, 1], [3, 5], [0, -10] )
    data = b.calcTrajectory( dt, steps )
    print("Time   X     Y")
    for entry in data:
        print("%5.2f %5.2f %5.2f" % entry )
    
    

if __name__ == "__main__":
    test1()
    test2()
    test3()
    main(sys.argv)
          

# Q6: Write the name of each item in the Ball class symbol table

# The Ball class ST contains an entry for each method
# __init__
# getPos
# setPos
# getVel
# setVel
# getAcc
# setAcc
# calcPos
# calcTrajectory


# Q7: Write the name and type for each item in the object symbol table
# referenced by the variable b in the test1 function.

# The object symbol table contains an entry for each field created in
# the __init__ method.

# pos  tuple
# vel  tuple
# acc  tuple
#
# there is also an implied reference to the Class symbol table

# Q8: Explain the process by which Python identifies the meaning of
# the name calcTrajectory in the test3 function

# The variable b references the object symbol table. When the name is
# not found in the object symbol table, then Python checks the
# object's class symbol table, which is where calcTrajectory defined.
