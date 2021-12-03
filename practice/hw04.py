# Homework 4

def eat( things ):
    whattoeat = things.pop()
    return whattoeat

def hungry( thingstoeat ):

    print("Eating things")
    for group in thingstoeat:
        while len(group) > 1:
            print( "Eating a " + eat( group ) + ". Tasty!" )

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


'''    
Q1: How many list objects are created in this code and where?

There are five lists created by this code by the assignments to
citrus, musa, runus, pome, and fruit. There are no other statements
where a list object is created.

Q2: What value does the function hungry return?

Since no explicit value is given to the return statement for the
hungry funtion, it will return the special value None.

Q3: at the line #mark 1, what expression using fruit would have the value 'cherry'?

'cherry' is the third and last value in the third sub-list of fruit.
Any of the following would be correct.

fruit[2][-1]
fruit[2][2]
fruit[-2][-1]
fruit[-2][2]


Q4: at the line #mark 1, what expression using fruit would have the value 'orange'?

'orange' is the first value of the second sublist of fruit. Any of the following
would be correct.

fruit[1][0]
fruit[1][-3]
fruit[-3][0]
fruit[-3][-3]

Q5: Write out the global symbol table with name and type only at #mark 1.

eat      function
hungry   function
citrus   list
musa     list
prunus   list
pome     list
fruit    list


Q6: Write out the hungry function symbol table, name and type only, at #mark 2
thingstoeat list
group       list
leftovers   list
i           int

Q7: how many items remain in the lists referenced by citrus, musa, prunus, and pome at #mark 3?

The while loop inside the first for loop exits when the length of the
sublist is equal to 1. Therefore each of the sub-lists will have only
one item in them.

'''
