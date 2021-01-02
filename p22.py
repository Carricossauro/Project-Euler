# Problem 22 - 1/1/2021
# No comment, easy problem to solve
#!/bin/python3

def solve(nameList,name):
    p = 0
    length = len(nameList)
    while p < length:
        if nameList[p] == name:
            break
        p+=1
    return (p != length) * (p+1) * score(name)

def score(name):
    return sum(map(lambda x: ord(x)-64,name))
    
# Receive list of names and order it
names = []
for _ in range(int(input())):
    names.append(input())
names.sort()

# Solve queries
for _ in range(int(input())):
    print(solve(names,input()))
