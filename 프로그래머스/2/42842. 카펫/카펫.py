def solution(brown, yellow):
    y_x = 0
    y_y = 0
    answer = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            y_x = yellow // i
            y_y = i
            if 2*y_x + 2*y_y+4 == brown:
                answer.append(y_x+2)
                answer.append(y_y+2)
                break
            answer.sort(reverse=True)
    return answer