# 1. 배열에 정수 x(x≠0)을 넣는다
# 2. 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거, 가장 작은 값이 여러개일 때는 가장 작은 수를 출력하고 그 값을 배열에서 제거

import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)