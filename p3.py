# Problem 3 - 20/12/2020
# Not entirely my algorithm, but my code
# HackerRank 5/6 Cases (TC1)
#!/bin/python3
import math
import sys

def solve(n):
    while n % 2 == 0:
        n/=2
    i = 3
    while i < math.sqrt(n):
        while n % i == 0:
            n/=i
        i+=2
    if (n >= 2):
        return int(n)
    return i

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(solve(n))
