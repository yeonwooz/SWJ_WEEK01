#1914 하노이탑

import math

N = int(input())

def hanoi_tower(N, start, mid, to):
    if N==1: 
        print(f"{start} {to}")
        return
    else:
        hanoi_tower(N-1, start, to, mid)
        print(f"{start} {to}")
        hanoi_tower(N-1, mid, start, to)
        

print(int(math.pow(2, N))-1)

if N<=20:
    hanoi_tower(N, 1, 2, 3)