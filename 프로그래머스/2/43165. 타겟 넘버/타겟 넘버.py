from collections import deque

def solution(numbers, target):
    return = 0
    queue = deque([(numbers[0], 0), (-numbers[0], 0)])
    while queue:
        value, idx = queue.popleft()
        if idx == len(numbers) -1:
            if value == target:
                result += 1
        else:
            idx += 1
            queue = [(value + numbers[idx], idx), (value - numbers[idx], idx)]
    return result
