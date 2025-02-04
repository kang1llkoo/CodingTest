import heapq

def solution(k, score):
    answer = []
    rank = []
    for sco in score:
        heapq.heappush(rank, sco)
        if len(rank) > k:
            heapq.heappop(rank)
        answer.append(rank[0])
    return answer