# CS 5001 Spring 2021
# Practice problems 7
#

MAK = 0
MOD = 1
COL = 2
NIC = 3

# returns a list with the make, model, color, and nickname as entries in the list
def Car( make='', model='', color='grey', nickname='car' ):
    return [ make, model, color, nickname ]

# update the make field of the car
def setMake( car, newmake ):
    car[MAK] = newmake

# update the model field of the car
def setModel( car, newmodel ):
    # Q1: write this function
    car[MOD] = newmodel

# update the color field of the car
def setColor( car, newcolor ):
    # Q2: write this function
    car[COL] = newcolor

# update the Nickname field of the car
def setNickname( car, newname ):
    # Q3: write this function
    car[NIC] = newname

def getMake( car ):
    return car[MAK]

# Q4: write the functions getModel, getColor, and getNickname
def getMake(car):
    return car[MAK]

def getModel(car):
    return car[MOD]

def getColor(car):
    return car[COL]

def getNickname(car):
    return car[NIC]

# Q5: write this function, which should return a string that is a
# phrase describing the car
def toString( car ):
    return "a " + getColor(car) + " " + getMake(car) + " " + getModel(car) + " named " + getNickname(car)


def main():

    car1 = Car( 'Toyota', 'RAV4', nickname = "my car" )
    car2 = Car( 'Nissan', 'Versa', nickname = "putt putt" )
    car3 = Car( 'Volkswagon', 'Beetle', color = "white", nickname = "Herbie" )
    car4 = Car()

    setMake(car4, 'Porsche' )
    setModel(car4, '911' )
    setNickname( car4, 'vroom' )

    print( "I like to drive", toString(car4) )
    print( "I don't like driving", toString(car2) )

    cars = [ car1, car2, car3, car4 ]
    print("\nAll Cars\n---------------------")
    # Q6: write a loop that prints out the make, model, color, and nickname of each car
    for car in cars:
        print( getMake(car) + ", " + getModel(car) + ", " + getColor(car) + ", " + getNickname(car) )

    # Q7: how many list objects have been created in the code at this point?
    #  Each of the four calls to Car creates one list. The assignment to cars creates a fifth list.


if __name__ == "__main__":
    main()
