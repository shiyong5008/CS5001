# CS 5001
# Fall 2020
# Homework #9
#

class Builder:
    def __init__(self, string, delimiter):
        self.storage = {}
        self.buildit( string, delimiter )

    def buildit(self, source, divider ):
        state = 'a'
        firstthing = ''
        secondthing = ''
        for c in source:
            if state == 'a':
                if c == divider:
                    state = 'b'
                else:
                    firstthing += c
            elif state == 'b':
                if c == divider:
                    state = 'a'
                    self.storage[firstthing] = secondthing
                    firstthing = ''
                    secondthing = ''
                else:
                    secondthing += c

    def update(self, dragon, bones):
        self.storage[bones] = dragon

class Cookies(Builder):
    def __init__(self, a, b):
        pairs = ''
        for i in range(len(a)):
            pairs += a[i] + '%' + b[i] + '%'
        Builder.__init__(self, pairs, '%')

class Soups(Builder):
    def __init__(self, q, r):
        george = ''
        for fred in range(len(q)):
            george += q[fred] + '@' + r[fred] + '@'
        Builder.__init__(self, george, '@')
        print( 'Question 5')
        for item in dir():
            print( item, type(eval(item)))


def main():            
    s = Soups( ['corn', 'clam', 'lobster'], ['chowder']*3 ) # mark 1
n
    c = Cookies( ['pecan', 'chocolate', 'raisin'], ['sandies', 'chip', 'oatmeal'] )

    s.update( 'with wild rice and smoked sausage', 'corn' )
    c.update( 'cherry cookies', 'chocolate' )
    c.update( 'cookies', 'sugar' ) # mark 2

    print( '\nQuestion 3', s.storage)
    print()
    print( 'Question 4')
    for item in dir(c):
        if not ("__" in item) or ("__init__" in item):
            print( item, type(eval('c.'+item)))

if __name__ == "__main__":
    main()

# Question 1: what does the method buildit do?

# Question 2: List all of the functions or methods that are executed by the line of code at # mark 1.

# Question 3: What would be the value of the expression s.storage at # mark 2?

# Question 4: List the name and type of the symbols in the symbol
# table for the object refereced by c at # mark 2.

# Question 5: What are all of the symbols in the __init__ method
# symbol table of the Soups class when it is called at # mark 1?

'''
Question 1: If the source input to the function is a string with the form 

<a><delimiter><b><delimiter>

repeated any number of times.  Then it will add to self.storage (a
dictionary) entries with the key <a> and the value <b>.  In other
words, it parses a string, separating it using the delimiter
characters into words, and builds key-value pairs out of neighboring
pairs of words.  Each odd word is a key and the following even word
is its value.

If you consider both the Cookies and Soups __init__ methods, both of
them take in two lists and build a string with a delimiter between the
words.  In the case of the Soups __init__, it is called with the lists

['corn', 'clam', 'lobster'] and ['chowder', 'chowder', 'chowder']

It then loops over both lists building the string

'corn@chowder@clam@chowder@lobster@chowder@'

which then gets turned into dictinary entries by the buildit method.

{'corn':'chowder', 'clam':'chowder', 'lobster':'chowder'}

In the case of the Cookies, the string created by the __init__ method is

'pecan%sandies%chocolate%chip%raisin%oatmeal'

and that gets turned into the dictionary

{'pecan':'sandies', 'chocolate':'chip', 'raisin':'oatmeal' }


Question 2: The first function called is the Soups __init__
method. That method calls three functions. The first is the len
function, len(q).  The second function called is the range function,
range(len(q)). The third function is the Builder.__init__ function.

Inside the Builder.__init__ function, it calls the buildit method,
self.buildit( string, delimiter ).  

There are no function calls inside the buildit function.


Question 3: The expression s.storage evaluates as the dictionary in
the Soups object referenced by s.  The Soups object dictionary starts
out as above

{'corn':'chowder', 'clam':'chowder', 'lobster':'chowder'}

but then the statement 

s.update( 'with wild rice and smoked sausage', 'corn' )

changes the value for the key 'corn'.  So the result at mark 2 is:

{'corn':'with wild rice and sausage', 'clam':'chowder', 'lobster':'chowder'}


Question 4: The object referenced by the variable c is a Cookie object.

The Cookie class inherits from the Builder class, which means a Cookie
object has the functions in both its own definition and the functions
defined in the Builder class.  There are three functions.

__init__
buildit
update

Note that a symbol table can have only one entry for any one symbol.
Therefore, the __init__ symbol can have only one meaning for a Cookie
object.  There are not two __init__ entries.  The one that is in the
Cookie object is a reference to the __init__ function of the Cookie
class.

The only other symbol in the Cookie object symbol table is
self.storage, which gets created in the Builder.__init__ function by
the statement

self.storage = {}

which means that storage is type dict (dictionary).  So the full
name/type symbol table for the Cookie object referenced by c is:

__init__ -> function
buildit  -> function
update   -> function
storage  -> dict


Question 5: A function symbol table always contains **all** parameters
as well as any local variables created by assignments or for loops
within the function.  The __init__ method of the Soups class contains
three parameters: self, q, and r.  The method also creates the symbol
george (george = '') and the symbol fred (for fred in range(len(q)):).

Given the arguments to the Soups call at the top level, then names and
types are as follows.

self   -> instance of Soups
q      -> list
r      -> list
fred   -> int
george -> str


'''
