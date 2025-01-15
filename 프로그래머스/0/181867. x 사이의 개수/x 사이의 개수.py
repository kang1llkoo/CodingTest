def solution(myString):
    answer = []
    myString = myString.replace('x', ' ')
    myString = myString.split(' ')
    for o in myString:
        answer.append(len(o))
    return answer