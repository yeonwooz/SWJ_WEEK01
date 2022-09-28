#1181 단어 정렬
#(?) sorted 안쓰고 구현 연습해보기

# 오후 4시 1분

import sys

n = int(sys.stdin.readline())
wordset=set()

for i in range (n):
    word = sys.stdin.readline().strip()
    wordset.add((len(word), word))

list = list(wordset)
sorted_list = sorted(list)

for e in sorted_list:
    (len, word) = e
    print (word)
    
# 오후 4시 20분