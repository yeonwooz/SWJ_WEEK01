#10819 차이를 최대로
# 오후 4시 45분

from itertools import permutations
import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))
max_sum = 0

def sum_of_per (ls, n):
    sum = 0
    for i in range(1,n):
        sum += abs(ls[i-1]-ls[i])
    return sum

for e in permutations(input_list, n):
    per = list(e)
    sumOfper = sum_of_per(per, n)
    if max_sum < sumOfper:
        max_sum = sumOfper

print(max_sum)

# 오후 5시 22분