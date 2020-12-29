# Problem 18 - 28/12/2020
# Brute-force method - Only effective because of small test samples -> 1<= n<= 15
# Problem 67 is the same thing but willl need to be optimized
#!/bin/python3

def solve(triangle,line,i,N):
    r = 0
    if line == N:
        r = triangle[line][i]
    elif i < 0 or i > line:
        r = 0
    else:
        r = triangle[line][i]
        es = solve(triangle,line+1,i,N)
        dr = solve(triangle,line+1,i+1,N)
	cond = es > dr
        r+= cond * es + (not cond) * dr
    return r

for _ in range(int(input())):
    trian = []
    for n in range(int(input())):
        trian.append([int(i) for i in input().split()])
    print(solve(trian,0,0,n))
