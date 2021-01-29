# Problem 28 - 29/01/2021
# 5/5 HackerRank Test Cases
# Sum[6 + (2 i + 1) (4 (2 i + 1) - 6), {i, 1, K}] on Wolfram Alpha
# a. Sum in every level is i^2 + (i-1)*i+1 + (i-2)*i+2 + (i-3)*i+3
# b. Because i is always odd, i=2k+1
# c. Replace i for 2k+1 in a.
# d. Sum of the resulting formula from k=1 to (N-1)/2 => odd numbers from 3 to N
# e. Add 1 for the middle number

m = 10**9+7
def spiral(N):
    K = (N-1)//2
    r = ((16 * K**3) + (30 * K**2) + (26 * K) + 3) // 3
    return r % m
        
for k in range(int(input())):
    N = int(input())
    print(spiral(N))
