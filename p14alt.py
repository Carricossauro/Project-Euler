# Problem 14 Alternative - 26/12/2020
# 11/11 HackerRank TC
# The power of memoization is incredible
#!/bin/python3

cache = []
cache = [0] * 5000000
cache[0] = 1
cache[1] = 2

solved=[]
solved = [0] * 5000000
solved[0] = 1
solved[1] = 2

def sequenceRecursive(x):
    r = 1
    if x < 5000000 and cache[x-1] != 0:
        r = cache[x-1]
    else:
        if x % 2 == 0:
            r += sequenceRecursive(x>>1)
        else:
            r += sequenceRecursive(3*x + 1)
        if x < 5000000:
            cache[x-1] = r
    return r    

def solve(x,y):
    m = cache[solved[x-2]-1]
    if m <= y:
        solved[x-1] = x
    else:
        solved[x-1] = solved[x-2]
        
    
for i in range(2,5000001):
    solve(i,sequenceRecursive(i))

k = int(input())
for _ in range(k):
    n = int(input())
    print(solved[n-1])
