#9020 골드바흐의 추측

import sys, math

def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 

a = int(sys.stdin.readline())

for i in range(a):
    n = int(sys.stdin.readline())
    a, b = n//2, n//2
    while a > 0:
        if is_prime(a) and is_prime(b):
            print (a, b)
            break
        a -= 1
        b += 1