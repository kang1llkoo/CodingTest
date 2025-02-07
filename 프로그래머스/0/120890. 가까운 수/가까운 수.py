def solution(array, n):
    closet = float('inf')
    for num in array:
        if abs(n-num) < abs(n-closet):
            closet = num
        elif abs(n-num) == abs(n-closet):
            closet = min(closet, num)
    return closet