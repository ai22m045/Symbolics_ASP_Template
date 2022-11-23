#script (python)

import clingo
N = clingo.Number

def gcd(a, b):
    if a.nummber == 0:
        return b
    else:
        na = a.number
        nb = b.number
        nc = nb%na
        return gcd(N(nc), a)
    

#end