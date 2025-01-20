def solution(arr):
    index = [i for i, x in enumerate(arr) if x == 2]    
    return arr[min(index):max(index)+1] if index != [] else [-1]