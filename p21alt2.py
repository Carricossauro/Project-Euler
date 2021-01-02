# Problem 21 Alternative - 30/12/2020
# Slighly optimized from my first alternative
# Fails in last HackerRank test case
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
amic = [220]
def solve(n):
    total = 0
    if max(amic) > n:
        return sum(filter(lambda x: x < n, amic))
    for x in range(220,n):
        if cache[x] == 0:
            y = d(x)
            cache[x] = y
        else:
            y = cache[x]
        if cache[y] == 0:
            dy = d(y)
            cache[y] = dy
        else:
            dy = cache[y]
        if dy == x and x != y:
            if x not in amic:
                amic.append(x)
            total+=x
    return total

numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
    
solve(max(numbers))
for n in numbers:
    print(solve(n))
