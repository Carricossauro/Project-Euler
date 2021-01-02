# Problem 21 - 30/12/2020
# Keeps timing out on HackerRank's last 2 test cases
# It works but apparently it's too slow
#!/bin/python3
from functools import reduce

limit = 10**5
suml = [0] * limit
a = [True] * limit
a[0] = a[1] = False
for i, isprime in enumerate(a):
    if isprime:
        for n in range(i*i, limit, i):
            a[n] = False
            
def d(n):
    keeper = n
    total = 0
    primeDivisors = []
    reducedA = filter(lambda x: x < n//2+1, a)
    if n == 1:
        total = 1
    else:
        for i, isprime in enumerate(reducedA):
            if n == 1:
                break
            if isprime:
                pair = (i,0)
                while n % i == 0:
                    pair = (i,pair[1]+1)
                    n //= i
                if pair[1] != 0:
                    primeDivisors.append(pair)
        
        sumPowers=[]     
        for x,y in primeDivisors:
            temp = (x**(y + 1) - 1)//(x - 1)
            sumPowers.append(temp)
        total = reduce(lambda x, y: x*y, sumPowers)-keeper
    return total

cache = [0] * 10**5
def solve(n):
    total = 0
    for x in range(220,n):
        y = d(x)
        dy = d(y)
        if cache[x] == 0:
            cache[x] = y
        if cache[y] == 0:
            cache[y] = dy
        if dy == x and x != y:
            total+=x
    return total
    
for _ in range(int(input())):
    n = int(input())
    print(solve(n))
