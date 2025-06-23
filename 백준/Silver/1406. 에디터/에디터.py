import sys
from collections import deque

# L: 커서를 왼쪽으로 한칸 옮김
# D: 커서를 오른쪽으로 한칸 옮김
# B: 커서 왼쪽에 있는 문자를 삭제
# P $: $라는 문자를 커서 왼쪽에 추가

string =  sys.stdin.readline().strip()
n = len(string)
m = int(sys.stdin.readline())
left = deque(string)
right = deque()

# abcd(c) abcdx(c) abcd(c)x abcdy(c)x

for command in range(m):
    command = sys.stdin.readline().strip().split()
    if command[0] == 'L':
        if left:
            right.appendleft(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.popleft())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] == 'P':
        left.append(command[1])

print(''.join(left+right))