from collections import deque

def solution(maps):
    def is_safe(x,y):
        return 0<=x<n and 0<=y<m and not visited[x][y] and maps[x][y]
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([(0,0)])
    visited[0][0] = 1
    distance = {(0,0):1}
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x,y = queue.popleft()
        for ddx, ddy in zip(dx, dy):
            nx = x + ddx
            ny = y + ddy
            if is_safe(nx,ny):
                if (nx,ny) == (n-1, m-1):
                    return distance[(x,y)] + 1
                queue.append((nx,ny))
                distance[(nx,ny)] = distance[(x,y)] + 1
                visited[nx][ny] = 1
    
    return -1