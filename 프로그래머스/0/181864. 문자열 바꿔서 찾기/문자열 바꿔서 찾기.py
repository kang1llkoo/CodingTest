def solution(myString, pat):
    string = ''.join('B' if char == 'A' else 'A' for char in myString)
    if pat in string:
        return 1
    else:
        return 0