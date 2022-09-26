#1978 소수 찾기

import sys, math

a = int(sys.stdin.readline())

inputlist = map(int, sys.stdin.readline().split())

def is_prime_number(x):
    if x == 1 : return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

cnt = 0
for e in inputlist:
    if is_prime_number(e) == True:
        cnt = cnt + 1