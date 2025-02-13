def solution(hp):
    troops = [5,3,1]
    count = 0
    for troop in troops:
        quodient, hp = divmod(hp, troop)
        count += quodient
    return count
        