def solution(order):
    prices = {
        'americano':4500,
        'cafelatte':5000,
        'anything':4500
    }
    answer = 0
    for item in order:
        if "americano" in item:
            answer += prices['americano']
        elif 'cafelatte' in item:
            answer += prices['cafelatte']
        elif item == 'anything':
            answer += prices["anything"]
    return answer