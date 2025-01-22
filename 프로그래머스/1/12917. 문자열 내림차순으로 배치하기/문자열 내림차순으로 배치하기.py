def solution(s):
    answer = ''
    s = sorted(s, reverse=True)
    for char in s:
        answer += char
    return answer