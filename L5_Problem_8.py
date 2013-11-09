'''
L5 Problem 8
------------

We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.

'''

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    aStrSorted = sorted(aStr)
    low = 0
    high = len(aStrSorted)
    mid = (low + high) / 2
    

    i = 0
    while i < 50:
        i += 1
        if len(aStr) <= 0:
            return False
            
        if char == aStrSorted[mid]:
            #print "Match! char = " + char + "  in " + str(aStrSorted)
            return True
        if (low == mid or high == mid) and (char != aStrSorted[mid]):
            #print "False"
            return False
        else:
            #print "not here"
            if char > aStrSorted[mid]:
                #print "char '"+ char +"'  is bigger than "+aStrSorted[mid]+", current low = " + str(low) + " , new Low = " + str(mid)
                low = mid
                return isIn(char, aStrSorted[low:high])

            else:
                #print "char '"+ char +"'  is smaller than "+aStrSorted[mid]+", current high = " + str(high) + " , new high = " + str(mid)
                high = mid
                return isIn(char, aStrSorted[low:high])

#Test Code
isIn('d', 'aagopssuy')

isIn('c', 'bbcdhiikllssxz')