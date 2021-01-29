# Problem 27 - 29/01/2021
# First try lol
# Easy brute force solve
# b is always prime because when n=0, n^2+na+b = b
# a is always even

limit = 100000
primes = [True] * limit
primes[0] = primes[1] = False
for i, isprime in enumerate(primes):
    if isprime:
        for n in range(i*i, limit, i):
            primes[n] = False

def numberOfPrimes(tup):
    a=tup[0]
    b=tup[1]
    n=0
    form = b
    while(primes[form]):
        n+=1
        form = n*(n+a)+b
    return (a,b,n)

def solve(N):
    r = (-1, 41, 42) # (a, b, number of consecutive primes)
    primeNums = [i for i,isprime in enumerate(primes[:N]) if isprime]
    for b in primeNums:
        for a in range(1,N+1,2):
            Pa = numberOfPrimes((a,b,n))
            Na = numberOfPrimes((0-a,b,n))
            p = Pa if Pa[2] > Na[2] else Na
            if p[2] > r[2]:
                r = p
    return r

N = int(input())
result = solve(N)
print(str(result[0]) + " " + str(result[1]))
