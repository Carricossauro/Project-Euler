# Problem 23 - 1/1/2021
# This took me a while to optimize but it finally passed all HackerRank test cases
#!/bin/python3
from functools import reduce

limit = 168
suml = [0] * limit
a = [True] * limit
a[0] = a[1] = False
for i, isprime in enumerate(a):
    if isprime:
        for n in range(i*i, limit, i):
            a[n] = False

# This comes from a previous problem
def sums(n):
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
        if sumPowers:
            total = reduce(lambda x, y: x*y, sumPowers)-keeper
    return total

abundants = []
for i in range(28123):
    if i > 1 and sums(i) > i:
        abundants.append(i)

def solve(n):
    r = "NO"
    smallerList = list(filter(lambda x: x < n,abundants))
    for x in smallerList:
        m = n-x
        if m in smallerList:
            r = "YES"
    return r
        
for _ in range(int(input())):
    n = int(input())
    if n > 28123:
        print("YES")
    else:
        print(solve(n))
