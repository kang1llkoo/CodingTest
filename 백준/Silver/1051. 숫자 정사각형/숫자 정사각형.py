n, m = map(int, input().split())

square = [list(map(int, input().strip())) for _ in range(n)]

max_size = 1

for i in range(n):
    for j in range(m):
        for l in range(1, min(n-i, m-j)):
            if square[i][j] == square[i][j+l] == square[i+l][j] == square[i+l][j+l]:
                max_size = max(max_size, (l+1)**2)

print(max_size)