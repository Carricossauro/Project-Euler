# Problem 28 - 29/01/2021
# 3/5 HackerRank Test Cases
# Doesn´t work on last 2 cases because of the high constraint for N

def spiral(x):
    r = 1
    while x > 1:
        x1 = x**2
        x2 = x1 - x + 1
        x3 = x2 - x + 1
        x4 = x3 - x + 1
        r += (x1 + x2 + x3 + x4)
        x -= 2
    return r % (10**9+7)
        
for k in range(int(input())):
    N = int(input())
    print(spiral(N))
