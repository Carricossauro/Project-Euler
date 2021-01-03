# Problem 24 Alternative - 3/1/2020
# This is my code, there is a problem but I don't know what it is
#!/bin/python3
from math import factorial

string = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
def fac(n):
    factoradical = [0]*13
    i = 13
    p = 0
    while i > 0:
        f = factorial(i)
        r,n = divmod(n,f)
        factoradical[p] = r
        p+=1
        i-=1
    return factoradical
    
def solve(s,n):
    r = ""
    ls = fac(n)
    for x in range(0,12):
        p = ls[x]
        r += s[p]
        s.pop(p)
    for x in s:
        r+=x
    return r

for _ in range(int(input())):
    n = int(input())
    s = string.copy()
    print(solve(s,n))
