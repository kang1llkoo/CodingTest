import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

while True:
    if room[x][y] == 0:
        room[x][y] = 2
        count += 1

    cleaned = False
    for _ in range(4):
        d = (d + 3) % 4 
        nx = x + dx[d]
        ny = y + dy[d]

        if room[nx][ny] == 0:  
            x, y = nx, ny
            cleaned = True
            break

    if not cleaned:
        back_dir = (d + 2) % 4
        bx = x + dx[back_dir]
        by = y + dy[back_dir]

        if room[bx][by] == 1:
            break
        else:
            x, y = bx, by

print(count)