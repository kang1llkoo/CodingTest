from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    return list((participant - completion))[0]