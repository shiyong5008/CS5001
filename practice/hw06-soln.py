
def mixer( a, b ):
    mixed = []
    while len(a) > 0 and len(b) > 0:
        mixed.append(a.pop())
        mixed.append(b.pop())

    while len(a) > 0:
        mixed.append( a.pop() )
    while len(b) > 0:
        mixed.append( b.pop() )

    return mixed

pancakes = [ ['flour', 'salt', 'sugar', 'baking powder', 'baking soda'], ['egg', 'buttermilk', 'oil'] ]
pancake_batter = mixer( pancakes[0][0:], pancakes[1][0:] )

biscuits = [ ['buttermilk', 'oil'], ['self-rising flour']]
biscuit_batter = mixer( biscuits[0], biscuits[1] )

print( "Pancake batter", pancake_batter[0:] )

print( "\nBiscuit batter" )
for item in biscuit_batter:
    print("  ", item[0:])

print()
print('pancakes', pancakes)
print('biscuits', biscuits)

# Q1: How many list objects are created in the above code, and on which lines are they created?

''' 
line 01: (2) The mixer function creates one list when it assigns
             an empty list to mixed.  It is called twice, so it creates 
             two new lists

line 13: (3) pancakes is assigned a list containing two lists

line 14: (2) pancakes[0] and pancakes[1] are indexed using slice notation to make a 
             copy of the two sublists inside pancakes.

line 16: (3) biscuits is assigned a list containing two lists

line 19: (1) The slice notation used on pancake_batter makes a copy of the list

Those are the only places where new list objects are created, which means the above 
code creates 11 list objects.
'''

# Q2: What does the function mixer do?

'''
Given two lists, it returns a new list that interleaves the elements from the two lists.  
The first item will come from list a, then list b, and so on.  If one list is longer than
the other, then any remaining items from the longer list go at the end.
'''


# Q3: What is the computational complexity of the mixer function? Explain
# your answer in terms of the length of a and the length of b.

'''
The function executes one append for each item in both lists.  As either list grows, 
the computational cost grows linearly along with it. We would call this function 
linear in the size of the lists, or O(N+M), if N and M are the length of the two lists.
'''

# Q4: Will both of the while loops at lines 06 and 08 execute?  Why/why not?

'''
Only one of the while loops will execute, because the first while loop will terminate 
only when one of the two lists has a length of zero.
'''

# Q5: What the value of pancakes at the end of the code?

'''
The pancakes list will have the same value it is assigned on line 13.

[ ['flour', 'salt', 'sugar', 'baking powder', 'baking soda'], ['egg', 'buttermilk', 'oil'] ]

It is not modified by the mixer function because a copy of the two sublists is passed
to the function.
'''

# Q6: What is the value of biscuits at the end of the code?

'''
The biscuits list will end up as a list of empty lists, because the sublists are are 
passed directly to the mixer function, which pops all of the items off both of its arguments.
'''


# Q7: Why is biscuits modified by the mixer function, while pancakes is not?

'''
A copy of the pancakes sublists are passed to the mixer function, so the original sublists are
not mdified.  The sublists of the biscuits list are passed directly, so they are modified.
'''

# Q8: What is a magic number and why is it good to replace them with variables?

'''
A magic number is any number (or string) literal in your code that is used to control
the functionality of the code.  A magic number may be used only once, but many are used
multiple times. 

Replacing every magic number with a variable has many benefits.

1. It means if the value is used in multiple locations it is easier to
avoid mistakes while coding because the variable is easier to remember
than the specific number.

2. If you need to change the number (or string) then if you are using
a variable you need to change only where the variable is assigned its
value and it will automatically be updated everywhere.  If the number
(or string) literal is hard-coded, then you have to change every
instance.
'''


