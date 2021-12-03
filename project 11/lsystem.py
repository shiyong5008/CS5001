# NEU CS5001 week8 project 11 lsystem.py version 4
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import sys
import random

class Lsystem:
    def __init__( self, filename = None ):
        # assign to the field base, the empty string
        self.base = ''
        # assign to the field rules, the empty list
        self.rules = { }
        # if the filename variable is not equal to None
        if filename!=None:
            # call the read method of self with filename as the argument
            self.read(filename)

    # Write the following mutator and accessor methods.
    def getBase(self):
        return self.base
    def setBase(self, b):
        self.base=b
    def getRule(self, index):
        return self.rules[index]
    def addRule(self, newrule):
        # self.rules={newrule[0]: newrule[1:]}
        self.rules[newrule[0]]=newrule[1:]

    # Create a method def numRules(self): that returns the number of rules in the rules list.
    def numRules(self):
        return len(self.rules)

    def read( self, filename ):
        # assign to the rules field of self the empty list
        self.rules={ }
        # assign to a variable (e.g. fp) the file object created with filename in read mode
        fp = open(filename, "r")
        lines = fp.readlines()
        # for each line in fp
        for line in lines:
            # assign to line the result of calling line.strip()
            strip_line = line.strip()
            # assign to a variable (e.g. words) the result of calling the split() method line
            words = strip_line.split(' ')
            # if the first item in words is equal to the string 'base'
            if words[0] == 'base':
                # call the setBase method of self with the new base string
                self.setBase(words[1])
            # else if the first item in words is equal to the string 'rule'
            elif words[0] == 'rule':
                # call the addRule method of self with the new rule (the slice of words from index 1
                self.addRule(words[1:])
        # call the close method of the file
        fp.close()

    def replace(self, istring):
        """ Replace all characters in the istring with strings from the
            right-hand side of the appropriate rule. This version handles
            parameterized rules.
        """
        tstring = ''
        parstring = ''
        parval = None
        pargrab = False

        for c in istring:
            if c == '(':
                # put us into number-parsing-mode
                pargrab = True
                parstring = ''
                continue
            # elif the character is )
            elif c == ')':
                # put us out of number-parsing-mode
                pargrab = False
                parval = float(parstring)
                continue
            # elif we are in number-parsing-mode
            elif pargrab:
                # add this character to the number string
                parstring += c
                continue

            if parval != None:
                key = '(x)' + c
                if key in self.rules:
                    replacement = random.choice(self.rules[key])
                    tstring += self.substitute(replacement, parval)
                else:
                    if c in self.rules:
                        replacement = random.choice(self.rules[c])
                        tstring += self.insertmod(replacement, parstring, c)
                    else:
                        tstring += '(' + parstring + ')' + c
                parval = None
            else:
                if c in self.rules:
                    tstring += random.choice(self.rules[c])
                else:
                    tstring += c

        return tstring

    # def replace(self, istring):
    #     # assign to a local variable (e.g. tstring) the empty string
    #     # tstring=[]
    #     tstring = " "
    #     # for each character c the original string (istring)
    #     for c in istring:
    #     # if the character c is in the self.rules dictionary
    #         if c in self.rules:
    #     # add to tstring a random choice from the dictionary entry self.rules[c]
    #             tstring += random.choice(self.rules[c])
    #     # else
    #         else:
    #     # add to tstring the character c
    #             tstring += c
    #     # return tstring
    #     return tstring

      # # assign to a local variable (e.g. tstring) the empty string
      #   tstring=[]
      # # for each character c in the input string (istring)
      #   for c in istring:
      #   # set a local variable (e.g. found) to False
      #       found = False
      #   # for each rule in the rules field of self
      #       for rule in self.rules:
      #     # if the symbol in the rule is equal to the character in c
      #           if c==rule[0]:
      #       # add to tstring the replacement from the rule
      #               tstring+=rule[1]
      #       # set found to True
      #               found = True
      #       # break
      #               break
      #   # if not found
      #       if not found:
      #     # add to tstring the character c
      #           tstring+=c
      # # return tstring, make sure this statement is not inside the for loop
      #   return tstring

    def buildString(self, iterations):
      # assign to a local variable (e.g. nstring) the base field of self
        nstring=self.base
      # for the number of iterations
        for i in range(iterations):
        # assign to nstring the result of calling the replace method of self with nstring as the argument
            nstring=self.replace(nstring)
      # return
        return nstring


    def substitute(self, sequence, value):
        """ given: a sequence of parameterized symbols using expressions
            of the variable x and a value for x
            substitute the value for x and evaluate the expressions
        """

        expr = ''
        exprgrab = False

        outsequence = ''

        for c in sequence:

            # parameter expression starts
            if c == '(':
                # set the state variable to True (grabbing the expression)
                exprgrab = True
                expr = ''
                continue

            # parameter expression ends
            elif c == ')':
                exprgrab = False
                # create a function out of the expression
                lambdafunc = eval('lambda x: ' + expr)
                # execute the function and put the result in a (string)
                newpar = '(' + str(lambdafunc(value)) + ')'
                outsequence += newpar

            # grabbing an expression
            elif exprgrab:
                expr += c

            # not grabbing an expression and not a parenthesis
            else:
                outsequence += c

        return outsequence

    def insertmod(self, sequence, modstring, symbol):
        """ given: a sequence, a parameter string, a symbol
            inserts the parameter, with parentheses,
            before each
            instance of the symbol in the sequence
        """
        tstring = ''
        for c in sequence:
            if c == symbol:
                # add the parameter string in parentheses
                tstring += '(' + modstring + ')'
            tstring += c
        return tstring


def main(argv):

    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read( filename )

    print( lsys )
    print( lsys.getBase() )
    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString( iterations )
    print( lstr )

    return

if __name__ == "__main__":
    main(sys.argv)