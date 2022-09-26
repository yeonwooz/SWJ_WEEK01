#2628 종이자르기

import sys

w,h  = map(int, sys.stdin.readline().split())

n = int(input())

x = [0, w]
y = [0, h]


for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a==1:
        x.append(b)
    elif a==0:
        y.append(b)

x.sort()
y.sort()

maxX=0
maxY=0

for i in range (0, len(x)-1):
    maxX = max(maxX, x[i+1]-x[i])

for i in range (0, len(y)-1):
    maxY = max(maxY,y[i+1]-y[i])


print (maxX*maxY)
