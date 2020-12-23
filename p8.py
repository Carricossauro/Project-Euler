# Problem 8 - 22/12/2020
#!/bin/python3

import sys

def solve(N,k,num):
    mult = 0
    
    for i in range(N-k):
        string = num[i:k+i]
        mul = 1
        for x in string:
            mul *= int(x)
        if mul > mult: mult = mul
    
    return mult

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()   
    print(solve(n,k,num))
