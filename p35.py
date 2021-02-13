# Problem 35 - 10/02/2021
# Almost as easy as 34, took me as couple minutes longer to write
# 6/6 HackerRank

limit = 10**6
prime = [True] * limit
prime[0] = prime[1] = False
for k,isprime in enumerate(prime):
    if isprime:
        for i in range(k*k,limit,k):
            prime[i] = False
            
N = int(input())

total = 0
for k in range(N):
    st = str(k)
    rotations = len(st)
    add = prime[k]
    for i in range(rotations - 1):
        if not add:
            break
        trade = st[0]
        st = st[1:] + trade
        x = int(st)
        if not prime[x]:
            add = False
    if add:
        total += k
        
print(total)
