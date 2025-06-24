import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
result = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(heap, -x)
    elif x == 0:
        if heap:
            result.append(-heapq.heappop(heap))
        else:
            result.append(0)

print('\n'.join(map(str, result)))