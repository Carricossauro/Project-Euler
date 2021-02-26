# Problem 39 Alternative - 16/02/2021
# This isn't even my code, it's suposed to work idk
from math import sqrt

def gcd(x, y):
    while(y):
        x, y = y, x % y
        return x

limit = 5 * 10**6
solutions = [0] * limit
for m in range(1,1201):
    start = 1 if m % 2 == 0 else 2
    for n in range(start,m,2):
        if gcd(m,n) == 1:
            k=1
            p = 2*m*(m+n)
            while k*p < 5*10**6:
                solutions[k*p] += 1
                k += 1

answer = [0] * limit
for i in range(1,limit):
    if solutions[i] > solutions[answer[i-1]]:
        answer[i] = i
    else:
        answer[i] = answer[i-1]

for k in range(int(input())):
    N = int(input())
    print(answer[N])
