# Bruce Maxwell
# CS 5001 Spring 2021
# Examples of symbol table access
#

# Python rule for symbol table access
# First rule: search the local symbol table
# Second rule: search the global symbol table

# Python rule for symbol creation/assignment
# First rule: without global keyword, a new symbol is created
# Second rule: with global keyword, the symbol in the GST is used, no local value is created

thing = 5

# does the assignment to thing create a new local variable or modify the global variable?
# the default action of python is to create a new local variable
def shadow():
    thing = 10
    print( "thing (shadow): ", thing)

# does this give an error (thing not defined) or does it search the global symbol table?
# the default is to check the global symbol if the variable is only accessed in the function
def access():
    temp = thing + 5
    print( "temp (access):", temp)
    print( "thing (access):", thing )

# does the first access look at the global symbol table?
# if a variable is assigned a value, it goes into the local symbol table, and all accesses 
# that variable must come after the assignment
def confusion():
    temp = thing + 5
    print( "temp (confusion):", temp)
    thing = 12
    print( "thing (confusion):", thing )

def moreconfusion():
    global thing  # this line says to look in the global symbol table for this name, and use it
    temp = thing + 5
    print( "temp (confusion):", temp)
    thing = 12
    print( "thing (confusion):", thing )


shadow()
print("thing (global):", thing)
access()
#confusion()
moreconfusion()
print("thing (global):", thing)

