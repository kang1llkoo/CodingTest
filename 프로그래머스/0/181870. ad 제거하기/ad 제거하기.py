def solution(strArr):
    answer = []
    for char in strArr:
        if 'ad' not in char:
            answer.append(char)
    return answer