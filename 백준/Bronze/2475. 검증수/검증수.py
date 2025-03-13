import sys

arr = list(map(int, sys.stdin.readline().split()))
answer = sum(x**2 for x in arr) % 10
print(answer)