# 1074 Z

import sys, math

N, r, c = map (int, sys.stdin.readline().split())

def func_z (r, c):
    if r==0 and c==0: return 0
    elif r==0 and c==1:  return 1
    elif r==1 and c==0: return 2
    elif r==1 and c==1: return 3
    else: 
        if r==0 : exp = int(math.log2(c))
        elif c==0 : exp = int(math.log2(r))
        else: exp = max(int(math.log2(r)), int(math.log2(c)))
        k = int(math.pow(2,exp))
        r_mod, c_mod = r%k, c%k
        r_quo, c_quo = r//k, c//k
        return func_z(r_mod, c_mod) + ( int(math.pow(4,exp)) * func_z(r_quo, c_quo) )

print(func_z(r,c))

