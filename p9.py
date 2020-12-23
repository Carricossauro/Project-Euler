# Problem 9 - 22/12/2020
# This is my 2nd attempt, still too slow
# HackerRank 3/8 Cases, because of speed issues
#!/bin/python3

import math
import sys

def solve(n):
    mult = -1
    aPower = 0
    for a in range(1,n//3):
        bPower = aPower
        aPower += a*2 - 1
        for b in range(a,n//2):
            bPower += b*2 - 1
            c2 = aPower + bPower
            c = math.sqrt(c2)
            if c.is_integer() and a+b+c == n:
                m = a*b*int(c)
                if m > mult: mult = m
                
    if mult == 0: mult = -1
    return mult

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
