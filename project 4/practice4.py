def eat( things ):
    whattoeat = things.pop()
    return whattoeat

def hungry( thingstoeat ):

    print("Eating things")
    for group in thingstoeat:
        while len(group) > 1:
            print( "Eating a " + eat( group ) + ". Tasty!" )
            print(group)

    # mark 3

    print( "What's left?" )
    for leftovers in thingstoeat:
        for i in range( len(leftovers) ):
            print("a " + leftovers[i] )
    # mark 2
    return

if __name__ == "__main__":
    citrus = [ 'orange', 'grapefruit', 'lemon' ]
    musa = [ 'banana', 'plantain' ]
    prunus = [ 'peach', 'plum', 'cherry' ]
    pome = [ 'apple', 'pear' ]
    fruit = [ musa, citrus ]
    fruit.append( prunus )
    fruit.append( pome )
    # mark 1
    hungry( fruit )

print(globals())