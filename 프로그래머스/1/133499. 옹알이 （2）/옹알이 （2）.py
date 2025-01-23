def solution(babbling):
    count = 0
    pros = ["aya", "ye", "woo", "ma"]
    for babble in babbling:
        for pro in pros:
            if pro * 2 in babble:
                break
            babble = babble.replace(pro, ' ')
        if not babble.strip():
            count += 1
    return count