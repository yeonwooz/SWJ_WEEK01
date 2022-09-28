#10989 수 정렬하기3
#내가 구현한 방식 : counting sort

import sys

n = int(sys.stdin.readline())
c = [0] * 10000

max_x = 1

for i in range (n):
    x = int(sys.stdin.readline())
    c[x-1] += 1
    if x > max_x: max_x = x

for i in range (0, max_x):
    cnt = c[i]
    for j in range (cnt):
        print (i+1)