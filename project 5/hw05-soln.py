# This homework is to practice some of the software engineering concepts
# and review material from the past six weeks
#

# Task 1: Write a function called sumListElements that takes in a list
# as an argument and returns the sum of the values in the list.  The
# summation should work for lists that contain only numeric values and
# it should work for lists that contain only string values.  If the
# process of summing the elements generates an error, the function
# should print an error message and return None
def sumListElements(q):
    try:
        sum = q[0]
        for item in q[1:]:
            sum += item
        return sum
    except:
        print("sumListElements(): cannot add all elements in the list")
        return None

# this is a function that will test sumListElements
def testSumListElements():
    q = [ i for i in range(10) ]

    print("sum should be 55:", sumListElements( q )  )

    q = [ chr(i) for i in range(97, 100)]
    print("sum should be abc:", sumListElements( q ) )

    q = [1, 2, "hi"]
    print("should generate an error message:", sumListElements( q ) )
    print()

    
# Task 2: Write a function concatStrings: given a list of strings,
# return a single string where all of the individual strings are
# concatenated together with a single space between each word.
# If the function generates an error message it should print an error
# message and return the empty string ''.  [Hint: look at the string
# strip method]
def concatStrings( s ):
    try:
        sout = s[0].strip()
        for item in s[1:]:
            item = item.strip()
            sout += ' ' + item
        return sout
    except:
        print("concatStrings(): unable to concatenate strings")
        return None

# test function for concatStrings
def testConcatStrings():
    s = [chr(i) for i in range(97, 105)]
    print("string should be 'a b c d e f g h':", concatStrings(s) )

    s = [ 'extra   ', '   spaces  ']
    print("string should be 'extra spaces':", concatStrings(s) )

    s = [ 1, 2 ]
    print("should cause an error message:", concatStrings(s) )

    s = []
    print("should cause an error message:", concatStrings(s) )
    print()


# Task 3: Write a function pigLatin. Given a single word, if the word
# begins with a vowel, add the suffix 'way'. If the word begins with a
# consonant, take all consonants before the first vowel, move them to
# the end of the string, and add the suffix 'ay'. If a y is the first
# letter, treat it as a consonant.  If a y is not the first letter, treat
# it as a vowel. The function should remove any initial or trailing spaces.
# example: computer -> omputercay
# example: python -> ythonpay
# example: chai -> aichay
# example: apple -> appleway
# example: outside -> outsideway
# if the function generates an error, it should return the empty string
# but it should not print an error message
def pigLatin( s ):
    try:
        s = s.strip()
        if s[0] in 'aeiou':
            return s + 'way'
        else:
            pre = s[0]
            i = 1
            while not s[i] in 'aeiou':
                pre += s[i]
                i += 1
            return s[i:] + pre + 'ay'
    except:
        return ''

# test function for pigLatin
def testPigLatin():

    words = [ 'computer', 'science', 'is', 'awesome', "y'all", 60 ]
    collect = ""
    for word in words:
        collect += pigLatin( word ) + ' '
    print( "output is:", collect )

    print("should be: omputercay iencescay isway awesomeway ally'ay\n" )


if __name__ == "__main__":
    testSumListElements()
    testConcatStrings()
    testPigLatin()
