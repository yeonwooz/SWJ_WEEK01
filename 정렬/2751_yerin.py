#2751 수 정렬하기2
#내가 구현한 방식 : quick sort _ random pivot

import sys
import random

N = int(sys.stdin.readline())
list = [ int(sys.stdin.readline()) for _ in range(N) ]

def quicksort (ls, start, end):
    if start >= end: 
        return
    else:
        pivot = random.randrange(start, end)
        ls[start], ls[pivot] = ls[pivot], ls[start]
        pivot = start
        left, right = start+1, end
        while left <= right:
            while left <= end and ls[left] <= ls[pivot]:
                left +=1
            while right > start and ls[right] >= ls[pivot]:
                right -=1
            if left > right:
                ls[pivot], ls[right] = ls[right], ls[pivot]
            else:
                ls[left], ls[right] = ls[right], ls[left]
        quicksort(ls, start, right-1)
        quicksort(ls, right +1, end)

quicksort(list, 0, N-1)

for e in list:
    print(e)


