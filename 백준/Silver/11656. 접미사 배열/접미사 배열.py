import sys

input = sys.stdin.readline

s = input().strip()
result = []

for i in range(0, len(s)):
    result.append(s[i:])

result.sort()

print('\n'.join(result))