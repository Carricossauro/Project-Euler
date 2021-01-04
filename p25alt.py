# Problem 25 Alternative - 3/1/2021
# Works 4/4 Test Cases
# O(1) because it only does the calculations once and then it accesses the list
#!/bin/python3
fibs = [0] * 5000
fibs[0] = 1

a = 1
b = 1
ib = 2
lengthToSearch = 2
while lengthToSearch < 5000:
    ib += 1
    b +=a
    a = b-a
    if len(str(b)) == lengthToSearch:
        fibs[lengthToSearch-1] = ib
        lengthToSearch+=1

for _ in range(int(input())):
    n = int(input())
    print(fibs[n-1])
