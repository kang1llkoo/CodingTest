import sys

x = int(sys.stdin.readline())

n = 1
while (n*(n + 1)) // 2 < x:
    n += 1

position = x - (n*(n - 1)) // 2

if n % 2 == 1:
    numerator = n - (position - 1)
    denominator = position
else:
    numerator = position
    denominator = n - (position - 1)

print(f"{numerator}/{denominator}")