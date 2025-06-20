import sys

n = int(sys.stdin.readline())
x_vals = []
y_vals = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    x_vals.append(x)
    y_vals.append(y)

width = max(x_vals) - min(x_vals)
height = max(y_vals) - min(y_vals)

print(width * height)