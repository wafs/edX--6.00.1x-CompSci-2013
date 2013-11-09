'''
L6 Problem 10
-------------
We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called howMany, which returns the sum of the number of values associated with a dictionary. For example:
'''

def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    counter = 0
    for e in aDict:
        counter += len(aDict[e])
    print counter
    return counter
    



#Test Code
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


howMany(animals)