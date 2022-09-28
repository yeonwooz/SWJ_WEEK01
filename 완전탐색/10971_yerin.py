#10971 외판원 순회 2

import sys
from itertools import permutations

INF = float('inf')
N = int(sys.stdin.readline())
input_matrix = []
cities = []
min_cost = INF

def calculate_cost (matrix, per, N):
    total_cost = 0
    for i in range (0, N-1):
        cost = matrix[per[i]][per[i+1]]
        if cost==0:
            total_cost = INF
            break
        else :
            total_cost += cost
    cost = matrix[per[N-1]][per[0]]
    if cost==0:
        total_cost = INF
    else : 
        total_cost += cost
    return total_cost
    

for i in range (N):
    input_matrix.append(list(map(int, sys.stdin.readline().split())))
    cities.append(i)

for e in permutations(cities, N):
    x = calculate_cost (input_matrix, list(e), N)
    if x < min_cost : 
        min_cost = x

print(min_cost)