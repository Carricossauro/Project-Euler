# Problem 2 - 20/12/2020
#!/bin/python3

import sys

def fibLowerN(N):
    fibs = []
    if N > 0:
        fibs.append(1)
        if N > 1:
            fibs.append(2)
            y = 3
            while (y < N):
                fibs.append(y)
                last2 = fibs[-2:]
                y = last2[0] + last2[1]
    return fibs
    
def solve(fibs):
    soma = 0
    for x in fibs:
        if (x % 2 == 0):
            soma += x
    return soma

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    listFibs = fibLowerN(n)
    print(solve(listFibs))
