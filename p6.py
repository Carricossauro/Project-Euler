# Problem 6 - 21/12/2020
#!/bin/python3

import sys

def solve(n):
    regularSum = n*(n+1)
    firstkSquares = regularSum*(2*n+1)
    firstkSquares//=6
    regularSum//=2
    return abs(regularSum**2 - firstkSquares)

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(solve(n))
