# Problem 1 - 19/12/2020
#!/bin/python3

import sys

numbers = []
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    numbers.append(n)

totals = []
for x in numbers:
    totalSum = 0
    for i in range(x):
        if i % 3 == 0 or i % 5 == 0:
            totalSum+=i
    totals.append(totalSum)
    
for num in totals:
    print(num)
