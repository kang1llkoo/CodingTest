from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []
chicken_shops = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chicken_shops.append((i, j))

min_chicken_distance = float('inf')

for selected_chicken_shops in combinations(chicken_shops, m):
    total_distance = 0

    for hx, hy in houses:
        min_distance = float('inf')

        for cx, cy in selected_chicken_shops:
            distance = abs(hx-cx) + abs(hy-cy)
            min_distance = min(min_distance, distance)
        
        total_distance += min_distance

    min_chicken_distance = min(min_chicken_distance, total_distance)

print(min_chicken_distance)