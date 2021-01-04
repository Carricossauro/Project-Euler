# Problem 25 - 3/1/2021
# This is too slow for the last case
# Still, works - 3/4 test cases
#!/bin/python3
cache = [0] * 20
cache[0] = 0
cache[1] = 1
cache[2] = 1
cache[3] = 2

def fib(n):
    r = 0
    if cache[n] != 0:
        r = cache[n]
    else:
        r = fib(n-1)+fib(n-2)
        cache[n] = r
    return r

for x in range(1,20):
    fib(x)
    
for _ in range(int(input())):
    n = int(input())
    cond = False
    x = 1
    while not cond:
        if len(str(fib(x))) == n:
            cond = True
        else:
            x+=1
    print(x)
