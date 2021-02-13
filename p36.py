# Problem 36 - 11/02/2021
# I was complicating this in my head lol, this a really wasy solution

def isPalindrome(word):
    return word == word[::-1]

def convertBase(b, Nword):
    rem = 0
    num = ""
    while Nword > 0:
        (div,rem) = divmod(Nword, b)
        num = str(rem) + num
        Nword = div
    return num

[N,K] = map(int, input().split())

total = 0
for p in range(1,N+1):
    st = str(p)
    if st == st[::-1]:
        newBase = convertBase(K,p)
        if newBase == newBase[::-1]:
            total += p

print(total)
