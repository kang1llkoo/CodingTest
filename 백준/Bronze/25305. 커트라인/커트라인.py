n, k = map(int, input().split())
x = list(map(int, input().split()))
# n: 응시자의 수
# k: 상을 받는 사람의 수

score = sorted(x, reverse=True)
print(min(score[:k]))