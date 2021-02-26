# Problem 40 - 16/02/2021
# My biggest problem was the numbers not being in ascending order lol
# 5/9 Test Cases, too slow for the missing ones
# But it's correct

def solve(digits):
    product = 1
    k = 1
    decimal = ""
    while digits != []:
        string = str(k)
        digitLength = len(string)
        digits = list(map(lambda x: x-digitLength, digits))
        check = list(filter(lambda x: x <= 0, digits))
        if check != []:
            for i in check:
                product *= int(string[i-1])
        digits = digits[len(check):]
        k += 1
    return product

for _ in range(int(input())):
    digits = list(map(int,input().split()))
    digits.sort()
    print(solve(digits))
