#2309 일곱 난쟁이
# 오후 4시 22분

from re import A
import sys

list = [ int(sys.stdin.readline()) for _ in range (9)]

sum_height = sum(list)
diff = sum_height - 100

for i in range (0,len(list)):
    a = list[i]
    b = diff-a
    if b in list:
        j = list.index(b)
        if i!=j:
            list.remove(a)
            list.remove(b)
            break

sorted_list = sorted(list)

for e in sorted_list:
    print (e)
    
# 오후 4시 40분
