# 1. 같은 눈이 3개 나오면 10000 + (같은 눈) * 1000
# 2. 같은 눈 2개 나오면 1000 + (같은 눈) * 100
# 3. 모두 다른 눈이면 (그 중 가장 큰 눈) * 100

n = int(input()) # 참여하는 사람 수
max_price = 0

for _ in range(n):
    dice = list(map(int, input().split()))
    dice.sort()

    if dice[0] == dice[1] == dice[2]:
        price = 10000 + dice[0] * 1000
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        price = 1000 + dice[1] * 100
    else:
        price = dice[2] * 100

    max_price = max(max_price, price)

print(max_price)