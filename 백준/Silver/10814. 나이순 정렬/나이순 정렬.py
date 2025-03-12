import sys

n = int(sys.stdin.readline().strip())

members = [tuple(sys.stdin.readline().split()) for _ in range(n)]
members.sort(key=lambda x: int(x[0]))

for age, name in members:
    print(age, name)