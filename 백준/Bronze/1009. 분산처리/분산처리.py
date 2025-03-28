import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    
    if a % 10 == 0:
        print(10)
    else:
        pattern = []
        num = a % 10
        while num not in pattern:
            pattern.append(num)
            num = (num * a) % 10
        index = (b - 1) % len(pattern)
        print(pattern[index])