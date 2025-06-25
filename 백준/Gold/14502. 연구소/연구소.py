from collections import deque
from itertools import combinations

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

empty = []
virus = []

for i in range(n):
    for j in range(m):
        if lab[i][j] == 0:
            empty.append((i, j))
        elif lab[i][j] == 2:
            virus.append((i, j))

def bfs():
    q = deque(virus)
    infected = []

    while q:
        x, y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
                lab[nx][ny] = 2
                infected.append((nx, ny))
                q.append((nx, ny))
    return infected

def get_safe_area():
    return sum(row.count(0) for row in lab)

max_safe = 0

for walls in combinations(empty, 3):
    for x, y in walls:
        lab[x][y] = 1

    infected = bfs()
    max_safe = max(max_safe, get_safe_area())

    for x, y in walls:
        lab[x][y] = 0
    for x, y in infected:
        lab[x][y] = 0

print(max_safe)