from collections import Counter

def solution(N, stages):
    result = {}
    counts = Counter(stages)
    users = len(stages)
    for stage in range(1, N+1):
        if users:
            count = counts.get(stage, 0)
            result[stage] = count / users
            users -= count
        else:
            result[stage] = 0
    return sorted(result, key = lambda x: result[x],reverse = True)