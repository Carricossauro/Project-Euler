# Problem 12 Alternative - 26/12/2020
# Still too slow, but more simple and faster than the first one
#!/bin/python3
import math

def divisors(n):
    div = 1
    for i in range(2,n+1):
        if n % i == 0:
            div+=1
    return div

def solve(n):
    x = 2
    tria = 1
    while divisors(tria) <= n:
        tria = (x * (x+1))//2
        x += 1
    return tria

for _ in range(int(input())):
    n = int(input())
    print(solve(n))
