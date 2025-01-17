def solution(arr):
    n = len(arr) #행
    m = len(arr[0]) #열
    if n > m:
        for i in range(n):
            for j in range(n-m):
                arr[i].append(0)
    else:
        for i in range(m-n):
            arr.append([0] * m)
    return arr