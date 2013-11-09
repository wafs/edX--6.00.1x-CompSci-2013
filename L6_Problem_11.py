'''
L6 Problem 11
-------------
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

Example usage:

>>> biggest(animals)
'd'

If there are no values in the dictionary, biggest should return None.
'''




def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = 0
    collection = []
    # Your Code Here
    if len(aDict) == 0:
        return None
    for e in aDict:
        if len(aDict[e]) >= biggest:
            biggest = len(aDict[e])
            collection = e


    return str(collection)
    
            

# Test Code
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


print biggest(animals)