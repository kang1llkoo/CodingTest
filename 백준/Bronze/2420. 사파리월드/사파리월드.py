import sys

n, m = map(int, sys.stdin.readline().split())

if n > m:
    print(n-m)
else:
    print(m-n)