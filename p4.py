# Problem 4 - 20/12/2020
# Brute-Force solution
# HackerRank 3/4 (TC3)
#!/bin/python3

import sys

lowerLimit = 100
upperLimit = 1000
    
def isPalindrome(x):
    stringX = str(x)
    return (stringX == stringX[::-1])

def solve(N):
    maxP = -2
    for x in range(upperLimit, lowerLimit,-1):
        for y in range(upperLimit, x-1,-1):
            mul = x*y
            
            if mul > N: continue
            if mul < maxP: break
            
            if isPalindrome(mul):
                maxP = mul
    return maxP

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(solve(n))
