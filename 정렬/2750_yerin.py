#2750 수 정렬하기
#내가 구현한 방식 : 버블 정렬

import sys

N = int(sys.stdin.readline())
list = [ int(sys.stdin.readline()) for _ in range(N) ]


for i in range (0, N):
    for j in range (1, N):
        if list[j-1] > list[j]:
            a = list[j-1]
            list[j-1] = list[j]
            list[j] = a
        i=i+1
        j=j+1

for e in list:
    print(e)