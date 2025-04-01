from collections import deque

n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 0
last_count = 0

while True:
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    melt = []
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if cheese[nx][ny] == 0:
                    queue.append((nx, ny))
                elif cheese[nx][ny] == 1:
                    melt.append((nx, ny))
    
    if len(melt) == 0:
        break
    
    last_count = len(melt)
    for x, y in melt:
        cheese[x][y] = 0
    
    time += 1

print(time)
print(last_count)