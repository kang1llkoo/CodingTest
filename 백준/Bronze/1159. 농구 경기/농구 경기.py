from collections import Counter

n = int(input())

names = [input().strip() for _ in range(n)]
first = [name[0] for name in names]
count = Counter(first)
valid = [letter for letter, cnt in count.items() if cnt >= 5]

if valid:
    print("".join(sorted(valid)))
else:
    print("PREDAJA")