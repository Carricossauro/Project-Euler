# Problem 5 - 21/12/2020
# That was so easy lol
#!/bin/python3

import sys

def mdc(x,y):
    while x != y:
        if x > y: x-=y
        else: y-=x
    return x

def mmc(x,y):
    return int((x*y)/mdc(x,y))

def solve(x):
    n = 1
    for i in range(2,x+1):
        n = mmc(n,i)
    return n

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
