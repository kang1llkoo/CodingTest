import sys
n = sys.stdin.readline().strip()
o = int(n, 8)
b = bin(o)[2:]
print(b)