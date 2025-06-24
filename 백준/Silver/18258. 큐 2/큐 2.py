from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

dq = deque()

for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push':
        dq.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        print(0 if dq else 1)
    elif cmd[0] == 'front':
        if dq:
            print(dq[0]) 
        else:
            print(-1)
    elif cmd[0] == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)