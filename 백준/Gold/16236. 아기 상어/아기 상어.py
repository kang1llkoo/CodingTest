from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0
x, y, size = 0, 0, 2

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x = i
            y = j

def bfs(x, y, baby_shark):
    dis = [[0] * n for _ in range(n)]
    vis = [[0] * n for _ in range(n)]

    q = deque()
    q.append((x, y))
    vis[x][y] = 1
    tmp = []
    while q:
        cur_x, cur_y = q.popleft()
        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and vis[nx][ny] == 0:
                if graph[nx][ny] <= baby_shark:
                    q.append((nx, ny))
                    vis[nx][ny] = 1
                    dis[nx][ny] = dis[cur_x][cur_y] + 1
                    if graph[nx][ny] < baby_shark and graph[nx][ny] != 0:
                        tmp.append((nx, ny, dis[nx][ny]))

    return sorted(tmp, key=lambda x: (-x[2], -x[0], -x[1]))

cnt = 0
res = 0
while 1:
    shark = bfs(x, y, size)
    if len(shark) == 0:
        break
    nx, ny, dist = shark.pop()

    res += dist
    graph[x][y], graph[nx][ny] = 0, 0
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0

print(res)