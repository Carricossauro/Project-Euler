# Problem 26 Alternative 2 - 28/01/2021
# 3/4 test cases
# only calculates the sequence length of primes because those are always bigger than the rest
# still too slow though
#!/bin/python3

limit = 10000
a = [True] * limit
a[0] = a[1] = False
for i, isprime in enumerate(a):
    if isprime:
        for n in range(i*i, limit, i):
            a[n] = False

lengthRec = [0]*limit
lengthRec[3] = 1
def solve(n):
    m=3
    for d,isprime in enumerate(a[:n]):
        if d <= 6 or not isprime:
            continue
        if lengthRec[d] == 0:
            p=1
            ex = 10
            while ex % d != 1:
                p+=1
                ex*=10
        else:
            p = lengthRec[d]
        if p > lengthRec[m]:
            m = d
            lengthRec[m] = p
    return m

for k in range(int(input())):
    n = int(input())
    print(solve(n))