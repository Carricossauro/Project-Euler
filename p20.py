# Problem 20 - 30/12/2020
# 1 minute - first try lol
#!/bin/python3

from math import factorial

def solve(n):
    numberString = str(factorial(n))
    total = 0
    for x in numberString:
        total += int(x)
    return total

for _ in range(int(input())):
    n = int(input())
    print(solve(n))
