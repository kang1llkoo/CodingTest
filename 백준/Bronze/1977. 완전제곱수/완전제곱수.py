import math

M = int(input())
N = int(input())

squares = [i**2 for i in range(math.ceil(math.sqrt(M)), math.floor(math.sqrt(N)) + 1) if M <= i**2 <= N]

# 출력
if squares:
    print(sum(squares))
    print(min(squares))
else:
    print(-1)