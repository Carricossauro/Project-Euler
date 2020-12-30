# Problem 19 - 29/12/2020
# HackerRank 5/8 Cases
#!/bin/python3

def century(date):
    dateS = str(date)
    return int(dateS[:-2])

def fixY(year):
    ye = str(year)[-2:]
    return int(ye)

def realMod(x):
    while x < 0:
        x+=7
    return x
    
def getWeekDay(d,m,y):
    c = century(y)
    year = fixY(y)
    return realMod((d + int(2.6 * m - 0.2) - 2 * c + year + year//4 + c//4) % 7)
    
def normalizeDate(d,m,y):
    if m < 3:
        y-=1
    m = m+10
    m = m % 12
    if m == 0: m = 12
    return (d,m,y)
       
def checkDates(d1,d2):
    r = False
    if d1[0] > d2[0]:
        r = True
    elif d1[0] == d2[0]:
        if d1[1] > d2[1]:
            r = True
        elif d1[1] == d2[1]:
            if d1[2] != 1:
                r = True
    return r

for _ in range(int(input())):
    sundays = 0
    d1 = [int(i) for i in input().split()]
    d2 = [int(i) for i in input().split()]
    if d1 == d2 and d1[2] == 1:
        ds,ms,ys = normalizeDate(1,d1[1],d1[0])
        weekDay = getWeekDay(ds,ms,ys)
        if weekDay == 0:
            print(1)
        continue
    elif checkDates(d1,d2):
        print(0)
        continue
    y = d1[0]
    if d1[2] == 1:
        mStart = d1[1] 
    else: mStart = d1[1]+1
    
    for m in range(mStart,13):
        ds,ms,ys = normalizeDate(1,m,y)
        weekDay = getWeekDay(ds,ms,ys)
        if weekDay == 0:
            sundays+=1
    for y in range(d1[0]+1,d2[0]):
        for m in range(1,13):
            d1,m1,y1 = normalizeDate(1,m,y)
            weekDay = getWeekDay(d1,m1,y1)
            if weekDay == 0:
                sundays+=1
    for m in range(1,d2[1]+1):
        d1,m1,y1 = normalizeDate(1,m,d2[0])
        weekDay = getWeekDay(d1,m1,y1)
        if weekDay == 0:
            sundays+=1
    print(sundays)
