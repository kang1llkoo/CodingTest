import sys

n = int(sys.stdin.readline())
people = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

ranks = [1]*n

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ranks[i] += 1

print(*ranks)