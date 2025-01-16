def solution(my_string, m, c):
    answer = ''
    temp = [my_string[i:i+m] for i in range(0, len(my_string), m)]
    for row in temp:
        answer += row[c-1]
    return answer