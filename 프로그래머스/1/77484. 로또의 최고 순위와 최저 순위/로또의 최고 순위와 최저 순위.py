def solution(lottos, win_nums):
    unknown = 0
    win = 0
    for num in lottos:
        if not num:
            unknown += 1
        elif num in win_nums:
            win += 1
            
    stand = [6,6,5,4,3,2,1]
    return [stand[win+unknown], stand[win]]