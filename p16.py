# Problem 16 - 28/12/2020
# I thought this was gonna be too slow for HackerRank, I'm somewhat confused
#!/bin/python3

def solve(n):
    x = str(2**n)
    total = 0
    for a in x:
        total += int(a)
    return total

for _ in range(int(input())):
    n = int(input())
    print(solve(n))
