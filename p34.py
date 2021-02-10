# Problem 34 - 10/02/2021
# Too easy, literally not a challenge lol
# 5/5 TC passed first try

from math import factorial as fact

N = int(input())

total = 0
for k in range(10,N):
    st = str(k)
    facts = 0
    for x in st:
        facts += fact(int(x))
    if facts % k == 0:
        total += k
        
print(total)
