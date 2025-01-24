def solution(s):
    count = 0
    me = 0
    other = 0
    for char in s:
        if me == other:
            count += 1
            pre = char
        if char == pre:
            me += 1
        else:
            other += 1
    return count