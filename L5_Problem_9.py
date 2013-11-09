'''
L5 Problem 9
------------

A semordnilap is a word or a phrase that spells a different word when backwards ("semordnilap" is a semordnilap of "palindromes"). Here are some examples:

nametag / gateman
dog / god
live / evil
desserts / stressed
Write a recursive program, semordnilap, that takes in two words and says if they are semordnilap.

This recursive function is not entirely straightforward. There are a few things that you need to check the first time you look at the inputs that you should not check on subsequent recursive calls: you need to make sure that the strings are not single characters, and also you need to be sure that the strings are not equal. If you do this check every time you call your function, though, this will end up interfering with the recursive base case (which we don't want!).

There's a few different ways you can perform checks on the inputs the first time. The first way would be to use keyword arguments. The second way would be to use a global variable, which you'll see in the next lecture video; however, using global variables is always a bit risky and thus not the best way to do this.

The third way to perform checks on the inputs the first time you see them, but not any subsequent time, is to use a wrapper function. This wrapper function performs some checks, then makes a call to the recursive function.

The idea of a wrapper function is really important. You'll see more wrapper functions later. To introduce you to the idea, we are providing you with the wrapper function; your job is to write the recursive function semordnilap that the wrapper function calls. Here is the wrapper function:

def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
Fill in the definition for semordnilap in the box below.

'''

def semordnilap(str1, str2):

    if len(str1) != len(str2):
        return False
        
        
    if(len(str1) > 0) and (len(str2) > 0):
        if len(str1) == 1:
            return str1 == str2
        if (str1[0] == str2[-1]):
            #print str1[0] +"   "+ str2[-1]
            return semordnilap(str1[1:], str2[:-1])

        else:
            #print "False"
            return False

