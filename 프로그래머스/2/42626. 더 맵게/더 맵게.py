import heapq

def solution(scoville, K):
    num_foods = len(scoville)
    heapq.heapify(scoville)
    score = heapq.heappop(scoville)
    idx = 0
    while idx < num_foods - 1 and score < K:
        heapq.heappush(scoville, score + heapq.heappop(scoville)*2)
        score = heapq.heappop(scoville)
        idx += 1
    return -1 if score < K else idx