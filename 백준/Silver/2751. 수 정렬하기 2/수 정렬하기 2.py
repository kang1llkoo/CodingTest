import sys

n = int(input())
answer = []

for _ in range(n):
    answer.append(int(sys.stdin.readline()))

for num in sorted(answer):
    print(num)