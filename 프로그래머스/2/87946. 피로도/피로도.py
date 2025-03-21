from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for perm in permutations(dungeons, len(dungeons)):
        curr = k
        count = 0
        for require, cost in perm:
            if curr >= require:
                curr -= cost
                count += 1
            else:
                break
        answer = max(answer, count)
    return answer