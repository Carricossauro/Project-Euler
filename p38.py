# Problem 38 - 12/02/2021
# A little confusing to write but overall easy stuff
# isPandigital came from an earlier problem though
# 6/6 TC

def isPandigital(s,n): # s is string to check, n is K
    l = []
    for i in s:
        if i not in l:
            l.append(i)
        else:
            return False
            break
    test = [str(i) for i in range(1,n+1)]
    fin = len(l)
    for i in test:
        fin -= 1
        if i not in l:
            return False
            break
    return fin == 0

def checkNumber(x,K):
    products = "0"
    i = 1
    num = "0"
    while len(products)-1 < K:
        num = str(x * i)
        products += num
        i += 1
    if isPandigital(products[1:],K):
        return True
    else:
        return False
    
[N,K] = map(int,input().split())
numbers = []

for k in range(2,N):
    if checkNumber(k,K):
        numbers.append(k)
        
numbers.sort()
for k in numbers:
    print(k)
