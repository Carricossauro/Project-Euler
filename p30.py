# Problem 30 - 31/01/2021
# Brute-force
# Works but I don't like it
N = int(input())

ini = 2**N + 1
lim = 1000000
tot = 0

for i in range(ini, lim):
    ls = str(i)
    som = 0
    while ls != "":
        k, ls = int(ls[-1]), ls[:-1]
        som += k**N
    if som == i:
        tot += i
        
print(tot)
