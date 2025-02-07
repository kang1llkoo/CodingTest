def solution(d, budget):
    count = 0
    for bud in sorted(d):
        budget -= bud
        if budget >= 0:
            count += 1
        else:
            break
    return count