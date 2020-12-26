# Problem 14 - 26/12/2020
# Works but it's too slow
#!/bin/python3

def sequence(x):
    r = 0
    while x != 1:
        if x % 2 == 0:
            x//=2
        else:
            x = 3*x+1
        r+=1
    return r

def solve(n):
    latest = 0
    k = 1
    for i in range(n,1,-1):
        seq = sequence(i)
        if seq > latest:
            latest = seq
            k = i
    return k

k = int(input())
for _ in range(k):
    n = int(input())
    print(solve(n))
