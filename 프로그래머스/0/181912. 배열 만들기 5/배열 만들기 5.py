def solution(intStrs, k, s, l):
    answer = []
    for strs in intStrs:
        num = int(strs[s:s+l])
        if num > k:
            answer.append(num)
    return answer