from collections import deque

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
max_height = max(max(row) for row in area)
result = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, height, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and area[nx][ny] > height:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

for h in range(0, max_height + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if not visited[x][y] and area[x][y] > h:
                bfs(x, y, h, visited)
                count += 1
    result = max(result, count)

print(result)