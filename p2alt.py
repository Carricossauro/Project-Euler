# Problem 2 Alternative - 20/12/2020
# Saw the algorithm online, had to try it
#!/bin/python3

import sys
    
def solve(N):
    x = 2
    previous = 0
    soma = 0
    while x < N:
        nextX = x * 4 + previous
        soma+=x
        previous = x
        x = nextX
    return soma  

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(solve(n))
