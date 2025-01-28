def solution(s):
    answer = [-1]*len(s)
    order = {}
    for idx, char in enumerate(s):
        if char in order:
            answer[idx] = idx - order[char]
        order[char] = idx
    return answer