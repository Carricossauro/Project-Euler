# Problem 12 - 25/12/2020
# I think it works but it's way too slow
# Tomorrow I'm gonna look for something better
#!/bin/python3
import math

divs = {}
divs[1] = 1
divs[2] = 2
limit = 10**5
triangles = {}
triangles[1] = 1
triangles[2] = 2

for i in range(3,limit):
    divs[i] = 2
    triangles[i] = triangles[i-1]+i
    for x in range(2,int(math.sqrt(i))+1):
        if i % x == 0:
            divs[i] += 2
            if i == x:
                divs[i]-=1
        
def solve(n):
    triangle = 1
    div = divs[1]
    i = 1
    while n >= div:
        i+=1
        triangle+=i
        div = divs[triangle]
    return triangle
    
for _ in range(int(input())):
    n = int(input())
    print(solve(n))
