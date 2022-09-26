#2869 달팽이는 올라가고 싶다

import sys, math

A, B, V = map(int, sys.stdin.readline().split())

day = 1
if V==A:
    print(day)
else:
    x = math.ceil((V-A)/(A-B)) #ceil : 올림 함수
    print(day+x)