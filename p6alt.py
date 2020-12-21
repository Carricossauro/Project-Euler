# Problem 6 Alternative - 21/12/2020
# This is too slow
#!/bin/python3

import sys

def solve(n):
    numbers = []
    sumOfSquares = 0
    sumNotSquared = 0
    for i in range(1,n+1):
        sumOfSquares += i**2
        sumNotSquared += i
    return abs(sumNotSquared**2 - sumOfSquares)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(solve(n))
