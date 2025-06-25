# 수빈이의 위치가 x일 때
# 걷는다면 1초 후 x-1 or x+1
# 순간이동을 한다면 1초 후 2*x

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100001
array = [0] * MAX

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)

print(bfs(n))