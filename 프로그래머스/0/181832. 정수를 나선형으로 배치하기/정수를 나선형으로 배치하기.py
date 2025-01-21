def solution(n):
    answer = [[0] * n for i in range(n)]     
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir = 0
    x, y = 0,0
    
    for i in range(1, (n*n)+1):
        answer[y][x] = i
        nx = x + dx[dir] 
        ny = y + dy[dir] 
        
        if nx<0 or ny<0 or nx>=n or ny>=n or answer[ny][nx] != 0:
            dir = (dir+1)%4 
            nx = x + dx[dir]
            ny = y + dy[dir] 

        x = nx
        y = ny

    return answer