'''
L6 Problem 2
------------
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. 

So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
'''

def oddTuples(aTup):
    i = 0
    newTup = ()
    for index in aTup:
        if i%2 == 0:
            newTup += (index,)
        i += 1
    return newTup

#Test Code
oddTuples((2, 2, 15, 18, 20))

oddTuples((1, 1, 12, 0, 2, 19, 20, 18))