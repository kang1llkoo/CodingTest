# 벽 또는 자기자신의 몸과 부딪히면 게임 종료
# 뱀은 처음에 오른쪽을 향한다
# 1. 뱀은 몸길이를 늘려 머리를 다음칸에 위치
# 2. 벽이나 자기자신의 몸과 부딪히면 게임 종료
# 3. 이동한 칸에 사과가 있다면 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
# 4. 이동한 칸에 사과 없으면 몸길이를 줄여 꼬리가 위치한 칸을 비운다

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direct, c):
    if c == 'L':
        return (direct -1) % 4
    else:
        return (direct + 1) % 4
    
n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)] 

for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1

l = int(input())
turns = dict()
for _ in range(l):
    x, c = input().split()
    turns[int(x)] = c

time = 0
direct = 0
snake = deque()
snake.append((0, 0))
board[0][0] = 2

x, y = 0, 0

while True:
    time += 1
    nx = x + dx[direct]
    ny = y + dy[direct]

    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        break

    if board[nx][ny] == 2:
        break

    if board[nx][ny] == 1:
        board[nx][ny] = 2
        snake.appendleft((nx, ny))
    else:
        board[nx][ny] = 2
        snake.appendleft((nx, ny))
        tx, ty = snake.pop()
        board[tx][ty] = 0

    x, y = nx, ny

    if time in turns:
        direct = turn(direct, turns[time])

print(time)