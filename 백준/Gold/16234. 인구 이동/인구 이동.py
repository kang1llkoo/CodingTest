import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    union = [(x, y)]
    total_population = A[x][y]

    while queue:
        cx, cy = queue.popleft()

        for i in range(4): 
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(A[cx][cy] - A[nx][ny]) <= R:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += A[nx][ny]

    new_population = total_population // len(union)

    for x, y in union:
        A[x][y] = new_population

    return len(union) > 1  

days = 0
while True:
    visited = [[False] * N for _ in range(N)]
    move_occurred = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):  
                    move_occurred = True

    if not move_occurred:
        break

    days += 1 

print(days)