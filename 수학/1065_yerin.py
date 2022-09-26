#1065 한수

import sys

input = sys.stdin.readline().strip()
input_list =  list(map(int, list(input)))
l = len(input)
a = int(input)

def is_han(ls):
    i = 0
    if int(ls[2])-int(ls[1]) == int(ls[1])-int(ls[0]):
        return True
    else: return False

if l < 3 :
    print (a)
else :
    cnt = 99
    for num in range (100, a+1):
        if is_han(str(num)): cnt=cnt+1
    print (cnt)
