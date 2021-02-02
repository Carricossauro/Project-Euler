# Problem 31 - 31/01/2021
# This isn't my code, but makes sense

k = int(input())

ways = [1]* (10**5 +1)

for x in [2,5,10,20,50,100,200]:
    for i in range(x, 100001):
        ways[i] += ways[i-x]
        
for i in range (k):
    l = int(input())
    print (ways[l]%(10**9+7))
