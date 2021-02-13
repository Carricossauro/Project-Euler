# Problem 37 - 12/02/2021
# Easy 5 min solve
# 4/4 TC

limit = 10**6
primes = [True] * limit
primes[0] = primes[1] = False
for k in range(2,limit):
    if primes[k]:
        for i in range(k*k,limit,k):
            primes[i] = False
            
N = int(input())
added = []
for k in range(11,N):
    word = str(k)
    wo = word
    truncable = True
    # Left to right
    while truncable and wo != "":
        num = int(wo)
        if not primes[num]:
            truncable = False
        wo = wo[1:]
    wo = word
    # Right to left
    while truncable and wo != "":
        num = int(wo)
        if not primes[num]:
            truncable = False
        wo = wo[:-1]
    if truncable:
        added.append(k)
        
print(sum(added))
