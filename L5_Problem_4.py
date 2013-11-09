'''
L5 Problem 4
------------

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. 
One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, 
and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
'''

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    c = min(a,b)
    
    while c > 0:
        if(a%c) == 0 and (b%c) == 0:
            return c
        else:
            c -= 1


#Test Cases

gcdIter(100, 140)

gcdIter(40, 44)

gcdIter(108, 48)