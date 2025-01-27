from collections import defaultdict

def solution(survey, choices):
    result = defaultdict(int)
    for typ, choice in zip(survey, choices):
        if choice < 4:
            result[typ[0]] += 4 - choice
        else:
            result[typ[1]] += choice - 4
    answer = ""
    for typ1, typ2 in ("RT", "CF", "JM", "AN"):
        answer += typ1 if result[typ1] >= result[typ2] else typ2  
    return answer