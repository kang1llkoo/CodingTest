import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    for _ in range(n):
        work = heapq.heappop(works)
        if work == 0:
            heapq.heappush(works, work)
            break
        heapq.heappush(works, work+1)
    return sum([work**2 for work in works])