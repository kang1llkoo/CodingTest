def solution(array, n):
    array.sort()
    answer = array[0]
    x = abs(n - array[0])
    for num in array:
        if x > abs(n - num):
            x = abs(n - num)
            answer = num
    return answer