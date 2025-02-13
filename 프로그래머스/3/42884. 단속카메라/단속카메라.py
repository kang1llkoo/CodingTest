def solution(routes):
    curr = 0
    numcam = 0
    
    routes = sorted(routes)
    for route in routes:
        if curr == 0:
            curr = route[1]
            numcam += 1
        elif route[1] <= curr:
            curr = route[1]
        elif route[0] > curr:
            numcam += 1
            curr = route[1]
            
    return numcam