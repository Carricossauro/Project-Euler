# Problem 15 - 27/12/2020
# This is not my code, I was not aware of the mathematical conclusion -> fact(m+n)/fact(m)*fact(n)
#!/bin/python3

from math import factorial as fact

for _ in range(int(input())):
    m, n = [int(j) for j in input().split(" ")]
    print((fact(m + n) // (fact(m) * fact(n))) % 1000000007)
