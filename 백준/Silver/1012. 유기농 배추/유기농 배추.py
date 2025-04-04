import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 함수
def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0  

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0  

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split()) 
    graph = [[0] * M for _ in range(N)] 

    for _ in range(K):
        y, x = map(int, input().split())
        graph[x][y] = 1 

    worm_count = 0 

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(i, j)
                worm_count += 1

    print(worm_count)