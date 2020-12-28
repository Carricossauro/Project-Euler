# Problem 17 - 28/12/2020
# What the f*ck is this lmao
#!/bin/python3
# 104 382 426 112
# One Hundred Four Billion Three Hundred Eighty Two Four Hundred Twenty Six One Hundred Twelve

numbers = {}
numbers[0] = "Zero"
numbers[1] = "One"
numbers[2] = "Two"
numbers[3] = "Three"
numbers[4] = "Four"
numbers[5] = "Five"
numbers[6] = "Six"
numbers[7] = "Seven"
numbers[8] = "Eight"
numbers[9] = "Nine"
numbers[10] = "Ten"
numbers[11] = "Eleven"
numbers[12] = "Twelve"
numbers[13] = "Thirteen"
numbers[14] = "Fourteen"
numbers[15] = "Fifteen"
numbers[16] = "Sixteen"
numbers[17] = "Seventeen"
numbers[18] = "Eighteen"
numbers[19] = "Nineteen"
numbers[20] = "Twenty"
numbers[30] = "Thirty"
numbers[40] = "Forty"
numbers[50] = "Fifty"
numbers[60] = "Sixty"
numbers[70] = "Seventy"
numbers[80] = "Eighty"
numbers[90] = "Ninety"

exponents = []
exponents.append("") # exponents[i] at i = 0
exponents.append("Thousand") # exponents[i] at i = 1
exponents.append("Million") # exponents[i] at i = 2
exponents.append("Billion") # exponents[i] at i = 3
exponents.append("Trillion") # exponents[i] at i = 4

def getNum(x,N):
    temp = ""
    if int(x) == 0:
        return temp
    elif int(x) in numbers.keys():
        return numbers[int(x)]
    elif N == 1:
        return numbers[int(x[0])]
    elif N == 2:
        if x[0] == '0':
            temp += numbers[int(x[1])]
        else:
            temp += numbers[int(x[0]) * 10]
            temp += " " + numbers[int(x[1])]
    elif N == 3:
        if x[0] == '0':
            temp += getNum(x[-2:],2)
        else:
            temp += numbers[int(x[0])] + " Hundred"
            tm = getNum(x[-2:],2)
            if tm:
                temp += " "
            temp += tm
    return temp
            
def solve(n):
    if int(n) in numbers.keys():
        return numbers[int(n)]
    final = ""
    triplets = []
    while n:
        triplets.append(n[-3:])
        n = n[:-3]
    exp = 0
    for x in triplets:
        temp = getNum(x,len(x))
        if temp:
            if exp > 0:
                temp += " " + exponents[exp]
            final = temp + " " + final
        exp+=1
    return final

for _ in range(int(input())):
    n = int(input())
    print(solve(str(n)))
