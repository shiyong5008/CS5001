def decline( youngNobles ):

    print( "Vin declines to dance with " + youngNobles.pop() )

def disappointment( suitors ):

    while len(suitors) > 1:

        decline( suitors )

        return suitors

def theBall( characters ):
    carriage = [ characters[0], characters[-1] ]
    print( carriage[1] + " gives " + characters[0] + " some final advice." )

    print( carriage.pop() + " heads into the night." )

    ball = [ characters[0], characters[1] ]

    print(ball[1][0])

    print( characters[0] + " enters the Venture ballroom." )

    unlikely = disappointment( ball[1] )
    print("??"+unlikely[1])

    print( characters[0] + " meets " + unlikely[0] + " on the balcony." )

    mistborn = [characters[0], characters[-1]]
    print( "After the ball, " + mistborn[1] + " leads " + mistborn[0] + " into the night." )

if __name__ == "__main__":
    characters = [ 'Vin', ['Eland','Young Noble 4','Young Noble 3','Young Noble 2','Young Noble 1'] ]

    characters.append( 'Kelsier' )
    theBall( characters )
    
print(globals())
print(characters[1][0])
