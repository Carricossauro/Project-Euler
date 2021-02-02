# Problem 32 - 01/02/2021
# 5/5 HackerRank Test Cases
# I'm not sure how, but I managed to make this work
# The constraints I found for b helped in the last case(n == 9), everything else worked fine before

def isPandigital(x,y,r,n):
    s = str(x) + str(y) + str(r)
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

n = int(input())
total = 0
added = []
    
ak = (n-1)//2
aLimit = 10 ** ak
for a in range(1,aLimit):
    aLen = len(str(a))
    # These constraints are not mine
    ####################################### 
    b_lower_digits = (n + 1) // 2 - 1  # minimum number of digits in b
    b_upper_digits = n // 2 + 1  # maximum number of digits in b
    bLower = 10 ** (b_lower_digits - aLen)
    bUpper = 10 ** (b_upper_digits - aLen)
    #######################################
    for b in range(bLower,bUpper):
        m = a*b
        if m not in added and isPandigital(a,b,m,n):
                total += m
                added.append(m)
            
print(total)
