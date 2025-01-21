def solution(arr):
    x = 0
    while(True):
        next = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                next.append(num/2)
            elif num < 50 and num % 2 != 0:
                next.append(num*2+1)
            else:
                next.append(num)
        if arr == next:
            return x
        else:
            x = x + 1
            arr = next