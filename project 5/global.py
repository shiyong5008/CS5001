thing = 5

def shadow( hi ):
    thing = hi + hi # adds thing to the shadow function symbol table
    print( "thing (shadow):", thing)
    return thing

def accessglobal( hi ):
    who = thing + hi  # only reading thing, accesses GST
    print("thing (accessglobal):", thing)
    return who

def accessBeforeAssign( what ):
    ranger = thing + what # causes an error b/c assignment makes thing local
    thing = what 
    return ranger

def booboo( what ):
    global thing  # tell the function to use the GST thing entry
    ranger = thing + what
    print( "thing (booboo):", thing )
    thing = what
    return ranger

def yogi( picnic ):
    global newvar # if newvar doesn't exist in the GST, it is added
    newvar = picnic + picnic
    return newvar

