# Problem 7 - 21/12/2020
# Personally don't like this solution but its seems to be the only available solution
# Could have used the Sieve of Eratosthenes, but I didn't
#!/bin/python3

import sys

def isPrime(n):
    r = True
    if (n != 2 and n % 2 == 0): r = False
    for i in  range(3, n//2, 2):
        if n % i == 0:
            r = False
            break
    return r

def nextPrime(n):
    if n % 2 == 0: n+=1
    while (not isPrime(n)):
        n+=2
    return n
    
primes = []
primes.append(2)
x = 3
for _ in range(10000):
    primes.append(x)
    x = nextPrime(x+1)
    
def solve(n):
    return primes[n-1]
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
