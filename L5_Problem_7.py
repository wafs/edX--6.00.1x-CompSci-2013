'''
L5 Problem 7
------------

For this problem, write a recursive function, lenRecur, which computes the length of an input argument (a string), by counting up the number of characters in the string.

Hint: String slicing may be useful in this problem...
'''

def lenRecur(aStr):
    s = aStr
    sLen = 0
    
    if s == '':
        return 0
    else:
        return 1 + lenRecur(s[0:-1]) #returns 1 + the amount of times this damn thing loops


#Test Code

lenRecur('')

lenRecur('siomweyqiypyryxnbqy')

Test: lenRecur('jxo')