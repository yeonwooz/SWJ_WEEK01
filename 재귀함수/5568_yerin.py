#5568 카드 놓기
#재귀로도 다시 풀어볼 것!!

from itertools import permutations

n = int(input())
k = int(input())
cards = [ input() for _ in range (n) ]

result = set()
card_permutation = permutations(cards, k)

for per in card_permutation:
    result.add(''.join(per))

print(len(result))