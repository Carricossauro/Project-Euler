# Problem 39 - 16/02/2021
# Works but is too slow
from math import sqrt

limit = 5 * 10**6 + 1
solutions = [0] * (limit-1)
p = 0
for a in range(1,limit):
    for b in range(1,a):
        c = sqrt(a*a + b*b)
        perimeter = int(a+b+c)
        if c.is_integer() and perimeter <= limit:
            solutions[perimeter] += 1
     
answer = [0] * (5 * 10**6)
higher = 0
for k in range(limit):
    if solutions[k] > solutions[higher]:
        higher = k
    answer[k] = higher
    

for k in range(int(input())):
    N = int(input())
    print(answer[N])
