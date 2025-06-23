# 오큰수: Ai보다 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수 / 없을 경우 -1 처리
# 3: 5 2 7 중 큰 수는 5 7 가장 왼쪽은 5
# 5: 2 7 중 큰 수는 7
# 2: 7 
# 7: -1

import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

result = [-1] * n
stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        result[idx] = nums[i]
    stack.append(i)

print(' '.join(map(str, result)))