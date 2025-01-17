def solution(arr, k):
    temp = []
    for i in arr:
        if i not in temp:
            temp.append(i)
        if len(temp) == k:
            break
    return temp + [-1] * (k - len(temp))