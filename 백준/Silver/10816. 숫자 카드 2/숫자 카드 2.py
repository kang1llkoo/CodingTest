import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

card_counter = Counter(cards)

result = [str(card_counter[target]) for target in targets]
print(' '.join(result))