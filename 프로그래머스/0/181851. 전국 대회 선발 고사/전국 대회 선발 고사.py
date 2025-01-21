def solution(rank, attendance):
    temp = sorted([(x, i) for i, x in enumerate(rank) if attendance[i] == True])
    return temp[0][1] * 10000 + temp[1][1] * 100 + temp[2][1]