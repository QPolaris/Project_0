#!/usr/bin/python3
#
# Project 0 is a set of small functions to warm up with python3 and discrete math.


# I Matthew Boyle have written all of this project myself, without any
# unauthorized assistance, and have followed the academic honor code.


import re, calendar, string, itertools


### Modify code below.


def phonenumber(s):
    """Converts formatted 10-digit phone numbers like '(123) 456-7890' to integers like 1234567890 or returns None when malformed"""
    if len(s) == 14:
        if re.match('\(\d{3}\) \d{3}-\d{4}', s):
            s = s.translate (str.maketrans ({c:None for c in string.punctuation}))
            s = s.translate (str.maketrans ({c:None for c in string.whitespace}))
            int(s)
            print (s)
            return s
        else:
            return None


def is_leapday(s):
    """Decides if a date/time like 'Mar 23, 2002 4:12:55am' is during a leap day
       Returns None when the date is invalid, True when it is a leap day, False otherwise"""
    '''if re.match('\w{3} ([1-9]|[1][0-9]|[2][0-9]|[3][0-1]), \d* ([1-9]|1[0-2]):[0-5][0-9]:\d{2}[ap]m', s):'''
    if re.fullmatch('((Jan|Mar|May|Jul|Aug|Oct|Dec) ([1-9]|[1][0-9]|[2][0-9]|[3][0-1])|(Apr|Jun|Sep|Nov) ([1-9]|[1][0-9]|[2][0-9]|[3]0)|(Feb ([1-9]|[1][0-9]|[2][0-9]))), \d* ([1-9]|1[0-2]):[0-5][0-9]:\d{2}[ap]m', s):
        l = s.split()
        if calendar.isleap(int(l[2])):
            if l[0] == 'Feb' and l[1] == '29,':
                return True
            else:
                return False
        else:
            return False
    else:
        return None


def evalsum(s):
    """Returns a string encoding a sum expression as a value."""
    if re.match('((\d*|.\d*|\d*.\d*)[-+])*', s):
        n = re.split('[+-]', s)
        o = re.split('[^+-]', s)
        Sum = float(n[0])
        step = 1
        for i in range(len(o)):
            if o[i] == '+':
                Sum = Sum + float(n[step])
                step = step+1
            elif o[i] == '-':
                Sum = Sum - float(n[step])
                step = step+1
        return Sum
    else:
        return None
            


def cuberoot(n):
    """Computes the cube root of float n by fixpoint iteration"""
    n2 = n
    new = (n/(n2**2)+(2*n2))/3
    while abs(n2) - abs(new) > 0.00000001:
        n2 = new
        new = (n/(n2**2)+(2*n2))/3
    return new

def helper(l):
    if len(l) <= 1:
        yield l
        yield []
    else:
        for item in helper(l[1:]):
            yield [l[0]]+item
            yield item
            
def powerset(st):
    """computes the power set of an input set st"""
    n = set(st)
    newlist = []
    while len(n) > 0:
        h = n.pop()
        newlist = newlist + [h]
    flist = (x for x in helper(newlist))
    flist = list(flist)
    newset = set()
    for i in range(len(flist)):
        newset.add(frozenset(flist[i]))
    return newset



def cartesianproduct(lst):
    """Takes a list of sets/frozensets and computes their Cartesian product"""
    new = set()
    for i in itertools.product(*lst):
        new.add(tuple(i))
    return new
    

def transitiveclosure(g):
    """computes the transitive closure of a graph/relation encoded as as a set of 2-tuples"""

    pass
