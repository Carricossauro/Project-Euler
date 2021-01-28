# Problem 26 - 28/01/2021
# 2/4 test cases
# works 100% sure but takes too long to calulate cache with 10k numbers
#!/bin/python3

limit = 1000

cache = [-1]*limit
cache[0] = 0
cache[1] = 0
cache[2] = 0
cache[3] = 1

def rep(x):
    d=x
    nums=[x]
    
    if cache[d] != -1:
        return cache[d]
    while(d % 10 == 0):
        d//=10
        nums.append(d)
    while(d % 2 == 0):
        d//=2
        nums.append(d)
    while(d % 5 == 0):
        d//=5
        nums.append(d)
    
    if cache[d] != -1:
        for k in nums:
            cache[k]=cache[d]
        return cache[d]
    
    if (d == 1):
        for k in nums:
            cache[k]=cache[d]
        return 0
    else:
        p=9
        while(p % d != 0):
            p*=10
            p+=9
        l=len(str(p))
        cache[d]=l
        for k in nums:
            cache[k]=cache[d]
        return l

for k in range(limit-1,4,-1):
    rep(k)

for k in range(int(input())):
    n = int(input())
    res = 0
    res = cache.index(max(cache[:n]),0,n)
    print(res)