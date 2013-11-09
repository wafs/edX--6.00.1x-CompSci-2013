'''
L5 Problem 6
------------
Although Python provides a built-in function for computing the length of a string, we can write our own.

Write an iterative function, lenIter, which computes the length of an input argument (a string), by counting up the number of characters in the string.
'''

def lenIter(aStr):
    s = aStr
    sLen = 0
    
    for c in s:
        sLen += 1
    return sLen




#Test Code
lenIter('')

lenIter('rbon')

lenIter('yyyihlgedjlazpqabwdm')