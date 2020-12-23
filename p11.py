# Problem 11 - 23/12/2020
# Got this on my first try, kinda proud :)
#!/bin/python3

import sys

def solve(grid):
    maxMult = 0
    for l,line in enumerate(grid):
        for x,y in enumerate(grid):
            con = l <= 16
            if x <= 16: 
                #Right (also makes up for left)
                mult = line[x]*line[x+1]*line[x+2]*line[x+3]
                if mult > maxMult:
                    maxMult = mult
                if con:
                    #Down-Right
                    mult = line[x]*grid[l+1][x+1]*grid[l+2][x+2]*grid[l+3][x+3]
                    if mult > maxMult:
                        maxMult = mult
            if con:
                #Down
                mult = line[x]*grid[l+1][x]*grid[l+2][x]*grid[l+3][x]
                if mult > maxMult:
                    maxMult = mult
            if x > 3 and con:
                #Down-Left
                mult = line[x]*grid[l+1][x-1]*grid[l+2][x-2]*grid[l+3][x-3]
                if mult > maxMult:
                    maxMult = mult
    return maxMult

grid = []
for grid_i in range(20):
    line = input().strip().split(' ')
    lineInt = [int(x) for x in line]
    grid.append(lineInt)
    
print(solve(grid))
