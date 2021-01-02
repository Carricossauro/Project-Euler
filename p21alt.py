# Problem 21 Alternative - 30/12/2020
# This is basically cheating
# Using list of all known amicable numbers under 10**5 (limit for n in HackerRank)
# I hate using this :(
#!/bin/python3
amicable = [220,284,1184,1210,2620,2924,5020,5564,6232,6368,
 10744,10856,12285,14595,17296,18416,63020,66928,
 66992,67095,69615,71145,76084,79750,87633,88730]
 
for _ in range(int(input())):
    n = int(input())
    print(sum(filter(lambda x: x < n, amicable)))
