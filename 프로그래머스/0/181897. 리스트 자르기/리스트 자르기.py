def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer
    if n == 1:
        answer.extend(num_list[0:b+1])
    elif n == 2:
        answer.extend(num_list[a:len(num_list)])
    elif n == 3:
        answer.extend(num_list[a:b+1])
    elif n == 4:
        answer.extend(num_list[a:b+1:c])
    return answer