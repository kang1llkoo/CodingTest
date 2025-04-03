import sys

n = int(sys.stdin.readline().strip())

length = 0
digit = 1
start = 1

while start <= n:
    end = min(n, start * 10 - 1)
    count = end - start + 1 
    length += count * digit
    digit += 1
    start *= 10

print(length)