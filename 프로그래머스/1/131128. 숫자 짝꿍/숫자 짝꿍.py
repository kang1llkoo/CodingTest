from collections import Counter

def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    common = x - (x - y)
    string = ""
    for key, value in common.items():
        string += key * value
    number = "".join(sorted(string, reverse=True))
    if number.startswith("0"):
        return "0"
    elif not number:
        return "-1"
    else:
        return number