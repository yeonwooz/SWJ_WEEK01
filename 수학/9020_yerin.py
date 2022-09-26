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
    half = int(n/2)
    a, b = half, half
    q=0
    while q < half:
        x, y = half-q, half+q
        if (x==y and is_prime(x)) or (is_prime(x) and is_prime(y)):
            a, b = x, y
            break
        q=q+1

    print ("{0} {1}".format(a,b))
