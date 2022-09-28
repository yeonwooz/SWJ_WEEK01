#2798 블랙잭

# 오후 4시 45분

from itertools import combinations
import sys

N, M = map ( int, sys.stdin.readline().split() )
list = list( map (int, sys.stdin.readline().split() ) )

max_sum=0

for (a, b, c) in combinations(list, 3):
    sum = a+b+c
    if sum > max_sum and sum <= M:
        max_sum = sum

print(max_sum)

# 오후 4시 56분